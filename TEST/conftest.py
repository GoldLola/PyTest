import json
import pytest


def load_credentials():
    credentials = json.load(open("config.json", "rb"))
    return credentials


@pytest.fixture
def page(page):
    credentials = load_credentials()
    username = credentials["username"]
    passwword = credentials["password"]
    page.goto(f"https://www.saucedemo.com/")
    return page

@pytest.fixture
def 