def fibonacci(n):
    # we check the Fibonacci initials which are always the same
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    # We make a loop to always add and give the result of the Fibonacci sequence
    a, b = 0, 1
    for _ in range(2, n + 1):
        c = a + b
        a, b = b, c
    return b

resultado = fibonacci(6)
print(resultado) 