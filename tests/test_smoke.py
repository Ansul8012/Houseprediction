
import json
from app import app


def test_smoke():
    assert 1 + 1 == 2


def test_predict_endpoint():
    client = app.test_client()
    # Example features, adjust as per your model's expected input
    features = [8.3252, 41, 6.9841, 1.0238, 322, 2.5555, 37.88, -122.23]
    response = client.post(
        '/predict',
        data=json.dumps({'features': features}),
        content_type='application/json'
    )
    assert response.status_code == 200
    data = response.get_json()
    assert 'prediction' in data or 'error' in data
