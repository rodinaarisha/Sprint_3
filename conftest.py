import pytest

@pytest.fixture
def name():
    name ='Test'
    return name

@pytest.fixture
def email():
    email = 'arina_rodina_09@yandex.ru'
    return email

@pytest.fixture
def password():
    password = '123456'
    return password
