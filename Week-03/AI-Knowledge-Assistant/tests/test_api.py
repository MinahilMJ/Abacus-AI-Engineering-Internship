from fastapi.testclient import TestClient

from api.main import app


client=TestClient(app)


def get_token():

    response=client.post(
        "/login",
        json={
            "username":"admin",
            "password":"admin123"
        }
    )

    return response.json()["access_token"]


def test_home():

    response=client.get(
        "/"
    )

    assert response.status_code==200


def test_invalid_file_upload():

    token=get_token()

    files={
        "file":(
            "test.jpg",
            b"fake image data",
            "image/jpeg"
        )
    }

    response=client.post(
        "/upload",
        files=files,
        headers={
            "Authorization":f"Bearer {token}"
        }
    )

    assert response.status_code==400