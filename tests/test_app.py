import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['MYSQL_HOST'] = "test"        # dummy values so test doesn't hit real DB
    app.config['MYSQL_USER'] = "test"
    app.config['MYSQL_PASSWORD'] = "test"
    app.config['MYSQL_DB'] = "test"
    with app.test_client() as client:
        yield client

# ✅ Test that the Flask app loads
def test_app_starts():
    assert app is not None

# ✅ Test home page redirect
def test_home_redirect(client):
    response = client.get('/')
    assert response.status_code in (200, 302)

# ✅ Test films route does not crash (it will render even if DB fails)
def test_films_route(client):
    response = client.get('/films')
    assert response.status_code == 200

# ✅ Test actors route
def test_actors_route(client):
    response = client.get('/actors')
    assert response.status_code == 200
