from http import HTTPStatus

import marshmallow
from flask import request, jsonify

from app import app
from app.core.services.db_methods import get_text_and_count, add_text_and_count
from app.schemas.text_and_count import TextAndCountSchema

texts_and_counts_schema = TextAndCountSchema(many=True)
text_and_count_schema = TextAndCountSchema()


@app.route("/api/counters/", methods=["GET", "POST"])
def counters():
    """
    Представление объектов TextAndCount.
    Разрешенные методы:
        - GET
        - POST -- data: {"text": <str>, "counter": <int>}
    """
    if request.method == "GET":
        posts = get_text_and_count()
        posts = texts_and_counts_schema.jsonify(posts)
        return posts, HTTPStatus.OK
    try:
        res = text_and_count_schema.load(request.get_json())
    except marshmallow.ValidationError as e:
        return jsonify({"error": e.messages}), HTTPStatus.BAD_REQUEST
    text_and_count = add_text_and_count(
        text=res["text"],
        counter=res["counter"],
    )
    return text_and_count_schema.jsonify(*text_and_count), HTTPStatus.CREATED
