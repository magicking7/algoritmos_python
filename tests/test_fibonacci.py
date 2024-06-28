from scripts.fibonacci import fibonacci

def test_first_2_numbers():
    res = fibonacci(2)
    assert res == [0,1]

def test_first_5_numbers():
    res = fibonacci(5)
    assert res == [0,1,1,2,3]

def test_first_10_numbers():
    res = fibonacci(10)
    assert res == [0,1,1,2,3,5,8,13,21,34]