import requests

ENDPOINT = "http://127.0.0.1:8000/"

def test_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    pass

def test_post_endpoint():
    payload = {
        "day": 7
        }
    response = requests.post(ENDPOINT + '/prediction', json = payload)
    assert response.status_code == 200
    
    data = response.json()
    print(data)
    pass

