from app import app
from werkzeug.datastructures import FileStorage
import io
import pytest

@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client

def test_upload(client):
    test_file = FileStorage(
        stream = io.BytesIO(b"abcdef"),
        filename="fileyfile.pdf",
        content_type="application/pdf"
    )
    rv = client.post("/hash", 
        data={"file": test_file},
        content_type="multipart/form-data"
        )
    json_data = rv.get_json()
    assert "data" in json_data
    assert 40 == len(json_data["data"][0]["sha1"])
    assert 6 == len(json_data["data"][0]["short_hash"])
    assert "filename" in json_data["data"][0]
    assert "version" in json_data

def test_root(client):
    json_data = client.get("/").get_json()
    assert "version" in json_data
    assert json_data["status"] == "ok"

def test_upload_error(client):
    rv = client.get("/hash")
    json_data = rv.get_json()
    assert 404 == rv.status_code
    assert "error" == json_data["status"]
