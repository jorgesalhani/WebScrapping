from src.pkg_web_scrapping import app

def test_health_check_init():
    res = app.req()
    assert res.status_code == 200