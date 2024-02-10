from http import HTTPStatus

from flask import jsonify

from . import app


@app.route("/", methods=["GET"])
def start():
    return jsonify({"app": "starts"}), HTTPStatus.OK
