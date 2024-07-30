import json
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import current_app

class DB:
    _conn = None

    @staticmethod
    def initialize():
        DB._conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            port=os.getenv('DB_PORT')
        )

    @staticmethod
    def get_connection():
        if DB._conn is None:
            DB.initialize()
        return DB._conn

    @staticmethod
    def get_cursor():
        conn = DB.get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        return conn, cursor

    @staticmethod
    def save_data(data):
        conn, cursor = DB.get_cursor()
        try:
            query = """
            INSERT INTO events (EventID, EventName, EventTime, Payload)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (data['event_id'], data['event_name'], data['event_ts'], json.dumps(data['payload'])))
            conn.commit()
        except Exception as e:
            current_app.logger.error(f"Error saving data to DB: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()