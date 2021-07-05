from pytest import mark


@mark.app_config
def test_environment(app_config):
    assert app_config.base_url == 'https://www.google.com/search?q=dev'
