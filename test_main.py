from fastapi.testclient import TestClient
import json
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Timothy Spengler": "DataHouse Assignment"}

def test_scores():
    test_data = None

    with open(f"./testing/test.json") as file:
        test_data = json.loads(file.read())

    response = client.post("/score/",json=test_data)
    assert response.status_code == 200
    assert response.json() == {'scoredApplicants': [{'name': 'John', 'score': 0.73},{'name': 'Jane', 'score': 0.98},{'name': 'Joe', 'score': 0.8},{'name': 'Timmy', 'score': 0.99}]}
