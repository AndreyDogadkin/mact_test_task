from http import HTTPStatus

from flask import jsonify, request

from app import app


@app.route("/api/counters/", methods=["GET", "POST"])
def get_counters():
    if request.method == "GET":
        return jsonify({"app": "starts"}), HTTPStatus.OK
    pass
