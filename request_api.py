"""
Blueprint contains views which serves API only.
"""
from datetime import datetime

from flask import Blueprint, jsonify, request


bp = Blueprint("request_api", __name__, url_prefix="/request")


@bp.route("/", methods=("POST",))
def create_request():

    email = request.form["email"]
    title = request.form["title"]

    # TODO: check if user exists
    # create if missing
    # check if order exists
    # create if missing

    return jsonify(
        email=email,
        title=title,
        id=str(4242),  # TODO: real user ID
        # TODO: strftime to configured format
        # TODO: real datetiem from db
        timestamp=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
    )


@bp.route("/", methods=("GET",))
def list_requests():
    return jsonify(
        requests=[
            dict(
                email="test@test.run",
                title="This is the title",
                id="4242",
                timestamp=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
            )
        ]
    )


@bp.route("/<request_id>", methods=("GET",))
def read_request(request_id):
    # TODO: get the object from data storage
    # TODO: add data storage :)
    return jsonify(
        email="test@test.run",
        title="This is the title",
        id="4242",
        timestamp=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
    )

@bp.route("/<request_id>", methods=("DELETE",))
def delete_request(request_id):
  """
  Delete request if it exsits. 404 otherwise.
  The spec asks for empty body, therefore, it can't be JSON.
  """
  return ''