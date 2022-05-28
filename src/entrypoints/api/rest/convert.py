import datetime
import uuid
import json
from flask import Blueprint, Response

from src.domain import model
from src.repository.memrepo import MemRepo
from src.use_cases.converted_list import converted_list_use_case
from src.serializers.model import ConvertedJsonEncoder

blueprint = Blueprint("convert", __name__)

def _get_converted_list():
    jpg = model.JPG(code=uuid.uuid4(), src_path="fake.jpg")
    pdf = model.PDF(code=uuid.uuid4(), dest_path="fake.pdf")
    return [
        {
            "converted_from": jpg,
            "converted_to": pdf,
            "converted_at": datetime.datetime.now()
        },
        {
            "converted_from": jpg,
            "converted_to": pdf,
            "converted_at": datetime.datetime.now()
        },
        {
            "converted_from": jpg,
            "converted_to": pdf,
            "converted_at": datetime.datetime.now()
        },
        {
            "converted_from": jpg,
            "converted_to": pdf,
            "converted_at": datetime.datetime.now()
        }
    ]

    
@blueprint.route("/converteds", methods=["GET"])
def converted_list():
    repo = MemRepo(_get_converted_list())
    result = converted_list_use_case(repo)
    return Response(
        json.dumps(result, cls=ConvertedJsonEncoder),
        mimetype="application/json",
        status=200
    )