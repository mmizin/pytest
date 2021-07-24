from pytest import mark


@mark.test_data
def test_television_turns_on(test_data):
    print(f'{test_data} turns on')


def test_browser_can_navigate_to_the_tg(browser):
    browser.get('https://www.google.com/search?q=training+group')