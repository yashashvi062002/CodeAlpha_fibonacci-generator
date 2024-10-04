def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    fib = fibonacci_generator()
    n_terms = 10  # Change this for more terms
    print("Fibonacci Series (Generator):")
    for _ in range(n_terms):
        print(next(fib))
