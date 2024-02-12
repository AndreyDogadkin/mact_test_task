from http import HTTPStatus

import marshmallow
from flask import request, jsonify

from app import app
from app.core.services.db_methods import DBMethods
from app.models.text_and_count import TextAndCount
from app.schemas.text_and_count import TextAndCountSchema

texts_and_counts_schema = TextAndCountSchema(many=True)
text_and_count_schema = TextAndCountSchema()

database = DBMethods()


@app.route("/api/counters/", methods=["GET", "POST"])
def counters():
    """
    Представление объектов TextAndCount.
    Разрешенные методы:
        - GET
        - POST -- data: {
                    "text": <str>,
                    "counter": <int>,
                    "local_time": <str, %H:%M:%S>,
                    "local_date": <str, %Y-%m-%d>
                  }
    """
    if request.method == "GET":
        posts = database.get_list_objs(model=TextAndCount)
        posts = texts_and_counts_schema.jsonify(posts)
        return posts, HTTPStatus.OK
    if not request.data:
        return (
            jsonify({"error": "JSON data is missing."}),
            HTTPStatus.BAD_REQUEST,
        )
    try:
        res = text_and_count_schema.load(request.get_json())
    except marshmallow.ValidationError as e:
        return jsonify({"error": e.messages}), HTTPStatus.BAD_REQUEST
    text_and_count = database.add_obj(
        model=TextAndCount,
        text=res["text"],
        counter=res["counter"],
        local_date=res["local_date"],
        local_time=res["local_time"],
    )
    return text_and_count_schema.jsonify(text_and_count), HTTPStatus.CREATED
