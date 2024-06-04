

def process(n: int) -> str:
    if (n % 3 == 0): return "Fizz"
    return n


def fizzbuzz() :
    
    for num in range(1, 101): print(process(num))