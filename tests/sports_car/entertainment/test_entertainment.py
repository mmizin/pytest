from pytest import mark

from selenium import webdriver


@mark.some_mark
def test_entertainment_function_as_expected():
    assert True


@mark.ui
def test_navigate_to_the_body_page(chrome_browser):
    chrome_browser.get('https://www.google.com/search?q=entertainment')