from sum_digits import sum_digits

def test_sum_digits():
    output = sum_digits([1, 2, 3])
    expected = 6

    assert output == expected, "Wrong answer"

def test_sum_digits_1():
    output = sum_digits([1, 5 ,4, 3, 2, 2, 3])
    expected = 20

    assert output == expected, "Wrong answer"