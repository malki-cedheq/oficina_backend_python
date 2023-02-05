# tests.py
'''
TDD
Test Driven Development
cli: pytest
'''
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_index():
    '''Teste Positivo'''
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Wordl"}


def test_login():
    '''Teste Negativo (não existe endpoint /login'''
    response = client.get("/login")
    assert response.status_code == 403
