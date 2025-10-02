from app import create_app

def test_homepage_ok():
    app = create_app("config.TestingConfig")
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Fresh Blogs" in resp.data
