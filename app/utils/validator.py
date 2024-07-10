from jsonschema import validate, ValidationError

def validate_schema(data, schema):
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        return e.message
    return None