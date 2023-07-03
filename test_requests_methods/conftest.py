import pytest
from request_page.request_page import RequestClass


@pytest.fixture( scope='session')
def _response():
    response = RequestClass()
    return response