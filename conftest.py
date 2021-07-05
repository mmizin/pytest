from pytest import fixture
from selenium import webdriver

from config import Config

def pytest_addoption(parser):
    parser.addoption('--env', action='store')


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
