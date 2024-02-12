import http
from datetime import datetime

import pytest


def test_can_get_counters(client, app_with_data):
    response = client.get("/api/counters/")
    assert response.status_code == http.HTTPStatus.OK
    assert len(response.json) == 1
    assert response.json[0]["text"] == "Testing text"
    assert response.json[0]["counter"] == 1


@pytest.mark.parametrize(
    "text, counter, local_date, local_time",
    [
        ("text1", 1, str(datetime.now().date()), str(datetime.now().time())),
        ("text2", 2, str(datetime.now().date()), str(datetime.now().time())),
        ("12321", 3, str(datetime.now().date()), str(datetime.now().time())),
        ("👀", 4, str(datetime.now().date()), str(datetime.now().time())),
    ],
)
def test_can_post_with_required_fields(
        client,
        text,
        counter,
        local_date,
        local_time,
):
    data = {
        "text": text,
        "counter": counter,
        "local_date": local_date,
        "local_time": local_time,
    }
    response = client.post("/api/counters/", json=data)
    assert response.status_code == http.HTTPStatus.CREATED
    assert response.json["text"] == text
    assert response.json["counter"] == counter


def test_cannot_post_counter_without_data(client):
    response = client.post("/api/counters/")
    assert response.status_code == http.HTTPStatus.BAD_REQUEST
    assert response.json["error"] == "JSON data is missing."


@pytest.mark.parametrize(
    "text, counter, local_date, local_time",
    [
        (None, 1, str(datetime.now().date()), str(datetime.now().time())),
        ("121", None, str(datetime.now().date()), str(datetime.now().time())),
        ("text1", 2, None, str(datetime.now().time())),
        ("text2", 3, str(datetime.now().date()), None),
    ],
)
def test_cannot_post_counter_without_required_fields(
        client,
        text,
        counter,
        local_date,
        local_time,
):
    data = {
        "text": text,
        "counter": counter,
        "local_date": local_date,
        "local_time": local_time,
    }
    response = client.post("/api/counters/", json=data)
    assert response.status_code == http.HTTPStatus.BAD_REQUEST
