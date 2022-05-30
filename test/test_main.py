import main
import numpy as np 
def test_main():
    expect = main.a
    output = "Hello world!"
    assert expect == output, "Wrong answer"

def test_main_1():
    expect = main.x
    output = np.array([[1, 2, 3], [4, 5, 6]])
    assert np.array_equal(expect, output), "Wrong answer"