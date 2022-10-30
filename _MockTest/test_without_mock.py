import time


def compute(x):
    response = expensive_api_call()
    return response + x


def expensive_api_call():
    time.sleep(1)
    return 123


def test_compute():
    expected = 124
    actual = compute(1)
    assert expected == actual
