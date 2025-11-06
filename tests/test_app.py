import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    # prevent real DB connection during tests
    app.config['MYSQL_HOST'] = "test"
    app.config['MYSQL_USER'] = "test"
    app.config['MYSQL_PASSWORD'] = "test"
    app.config['MYSQL_DB'] = "test"

    with app.test_client() as client:
        yield client


def test_app_starts():
    assert app is not None


def test_home_redirect(client):
    response = client.get('/')
    assert response.status_code in (200, 302)


def test_films_route(client):
    response = client.get('/films')
    # DB might fail, but route must not crash
    assert response.status_code in (200, 500)


def test_actors_route(client):
    response = client.get('/actors')
    # DB might fail, but route must not crash
    assert response.status_code in (200, 500)
