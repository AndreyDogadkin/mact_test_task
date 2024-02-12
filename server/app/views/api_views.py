from http import HTTPStatus

import marshmallow
from app.core.services.db_methods import DBMethods
from app.models.text_and_count import TextAndCount
from app.schemas.text_and_count import TextAndCountSchema
from flask import request, jsonify

from app import app

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
                    "local_time": <time>,
                    "local_date": <date>
                  }
    """
    if request.method == "GET":
        posts = database.get_list_objs(model=TextAndCount)
        posts = texts_and_counts_schema.jsonify(posts)
        return posts, HTTPStatus.OK
    try:
        res = text_and_count_schema.load(request.get_json())
    except marshmallow.ValidationError as e:
        return jsonify({"error": e.messages}), HTTPStatus.BAD_REQUEST
    text_and_count = database.add_obj(
        model=TextAndCount,
        text=res["text"],
        counter=res["counter"],
    )
    return text_and_count_schema.jsonify(text_and_count), HTTPStatus.CREATED
