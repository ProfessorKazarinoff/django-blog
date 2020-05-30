from django.test import TestCase

import pytest
from django.test import Client
c = Client()

def test_with_client(c):
    response = client.get('/')
    assert response.status_code == 200
