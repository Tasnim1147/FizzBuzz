from fizzbuzz import process


def test_one():
    assert(process(1) == 1)
    
    
def test_simple_numbers():
    
    assert(process(2) == 2)
    assert(process(5) == 5)
    assert(process(7) == 7)
    
    
def test_fizz_exclusive():
    
    assert(process(3) == "Fizz")
    assert(process(6) == "Fizz")
    assert(process(9) == "Fizz")