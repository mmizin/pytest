from pytest import mark


@mark.smoke
@mark.engine
def test_engine_function_as_expected():
    assert True
