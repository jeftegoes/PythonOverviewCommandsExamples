import mock_examples.slow
from mock_examples.main import slow_function


def test_slow_function_mocked_api_call(mocker):
    mocker.path('mock_examples.slow.api_call', return_value=5)

    expected = 5

    actual = slow_function()
    assert expected == actual
