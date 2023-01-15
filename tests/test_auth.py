from ..src.webscrapping.authentication import auth_google

def test_request_ok():
    res = auth_google.google_get()
    assert res.status_code == 200
