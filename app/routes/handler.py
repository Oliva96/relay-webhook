import json
from flask import Blueprint, request, jsonify, current_app

from ..schemas.schema1 import schema1
from ..utils.validator import validate_schema
from ..utils.s3 import S3
from ..utils.db import DB
from ..utils.decorators import login_required

bp = Blueprint('handler', __name__)

@bp.route('/handler', methods=['POST'])
@login_required
def handle_post():
    data = request.json
    errors = validate_schema(data, schema1)
    if errors:
        return jsonify({"errors": errors}), 400

    try:
        s3_client = S3.get_client()

        event_id = data['event_id']
        s3_bucket = current_app.config['S3_BUCKET']
        s3_key = current_app.config['S3_KEY']

        s3_client.put_object(Bucket=s3_bucket, Key=f'{s3_key}/{event_id}.json', Body=json.dumps(data))
        DB.save_data(data)

        return jsonify({"message": "Request processed successfully", "sent_json": data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


