import Program


def test_even():
    # Arrange
    a = 10
    b = 20

    # Act
    result = Program.sum_values(a, b)

    # Assert
    assert result == 30


def test_even_error():
    # Arrange
    a = 10
    b = "20"

    # Act
    result = Program.sum_values(a, b)

    # Assert
    assert result == "Invalid input."
