import mock_examples.functions as functions


def test_mocking_constant_a(mocker):
    mocker.patch.object(functions, "CONSTANT_A", 2)
    expected = 4
    actual = functions.double()

    assert expected == actual
