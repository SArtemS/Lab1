from .. import calculate


def test_c():
    assert calculate(
        4, 0, '/'
    ) == 'Деление на ноль невозможно', "На выходе должно быть 'Деление на ноль невозможно'"