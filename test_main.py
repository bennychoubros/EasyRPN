from fastapi.testclient import TestClient
from app.main import app

test_client = TestClient(app)

def test_root():
    response = test_client.get("/api/healthchecker")
    assert response.status_code == 200
    assert response.json() == {"message": "The API is LIVE!!"}

def test_read_root():
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the EasyRPN API. Try route /docs for more infos"}

# TODO: assert response csv
def test_download_results_in_csv_file():
    response = test_client.get('/results')
    assert response.status_code == 200

# Calculs testing
def test_sum():
    response = test_client.post(
        '/calculate',
        json={
            "operation_list": [
                1, 2, "+"
                ]
            }
        )
    assert response.status_code == 201
    assert response.json()['result'] == 3.0

def test_diff():
    response = test_client.post(
        '/calculate',
        json={
            "operation_list": [
                2, 1, "-"
                ]
            }
        )
    assert response.status_code == 201
    assert response.json()['result'] == 1.0

def test_mul():
    response = test_client.post(
        '/calculate',
        json={
            "operation_list": [
                3, 10, 5, "+", "*"
                ]
            }
        )
    assert response.status_code == 201
    assert response.json()['result'] == 45.0

def test_div():
    response = test_client.post(
        '/calculate',
        json={
            "operation_list": [
                3, 10, 5, "+", "/"
                ]
            }
        )
    assert response.status_code == 201
    assert response.json()['result'] == 5.0

def test_neg_number():
    response = test_client.post(
        '/calculate',
        json={
            "operation_list": [
                3, 10, -5, "+", "*"
                ]
            }
        )
    assert response.status_code == 201
    assert response.json()['result'] == 15.0

def test_complex():
    response = test_client.post(
        '/calculate',
        json={
            "operation_list": [
                3, -1, 2.0, "+", 4, "*", "+"
                ]
            }
        )
    assert response.status_code == 201
    assert response.json()['result'] == 7.0

def test_unknown_symbol():
    response = test_client.post(
        '/calculate',
        json={
            "operation_list": [
                3, 10, 5, "+", "*", "@"
                ]
            }
        )
    assert response.status_code == 422