import json

from pytest import fixture
from selenium import webdriver

from config import Config


def pytest_addoption(parser):
    parser.addoption('--env', action='store')


def load_test_data(path):
    with open(path) as file:
        data = json.load(file)
        return data


@fixture()
def chrome_browser():
    browser = webdriver.Chrome()
    return browser


@fixture(scope='session')
def env(request):
    print(f'HERE ::: {request.config.getoption("--env")}')
    return request.config.getoption('--env')


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg


@fixture(params=[webdriver.Chrome, webdriver.Firefox])
def browser(request):
    driver = request.param
    yield driver()
    driver().quit()


@fixture(params=load_test_data('tests/test_televisions/test_data.json'))
def test_data(request):
    data = request.param
    return data
