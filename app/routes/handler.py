from flask import Blueprint, request, jsonify
from ..schemas.schema1 import schema1
from ..utils.validator import validate_schema

bp = Blueprint('handler', __name__)

@bp.route('/handler', methods=['POST'])
def handle_post():
    data = request.json
    errors = validate_schema(data, schema1)
    if errors:
        return jsonify({"errors": errors}), 400

    # Process the request
    return jsonify({"message": "Handler1 processed successfully", "sent_json": data}), 200