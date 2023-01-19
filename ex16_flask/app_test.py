# app.py
'''
TDD
Test Driven Development
cli: pytest
'''
from app import app


def test_index():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.data == b'{"message":"Hello Wordl"}\n'
