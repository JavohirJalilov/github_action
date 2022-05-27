from unittest import expectedFailure
import main

def test_main():
    expect = main.a
    output = "Hello world"
    assert expect == output, "Wrong answer"