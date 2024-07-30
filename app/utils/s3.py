import boto3

class S3:
    __client = None

    @classmethod
    def connect(cls):
        cls.__client = boto3.client('s3')
        return cls.__client

    @classmethod
    def get_client(cls):
        if cls.__client:
            return cls.__client
        else:
            return cls.connect()
