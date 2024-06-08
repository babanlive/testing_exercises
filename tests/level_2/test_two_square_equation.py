import pytest

from functions.level_2.two_square_equation import solve_square_equation


@pytest.mark.parametrize(
    "square_coefficient, linear_coefficient, const_coefficient, expected",
    [
        (0, 0, 0, (None, None)),
        (0, 0, 1, (None, None)),
        (0, 1, 0, (0, None)),
        (1, 0, 0, (0, 0)),
        (1, 1, 0, (-1, 0)),
        (1, 1, 1, (None, None)),
        (2.5, 4.5, 2, (-1, -0.8)),
    ],
)
def test__solve_square_equation__valid_coefficients(
    square_coefficient, linear_coefficient, const_coefficient, expected
):
    assert (
        solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
        == expected
    )


@pytest.mark.parametrize(
    "square_coefficient, linear_coefficient, const_coefficient",
    [
        ("abc", 1, 1),
        (1, "abc", 1),
        (1, 1, "abc"),
        ("1", "None", "1"),
        ("1", "1", ""),
        ("1", "1", " "),
    ],
)
def test__solve_square_equation__invalid_coefficients(
    square_coefficient, linear_coefficient, const_coefficient
):
    with pytest.raises(TypeError):
        solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
