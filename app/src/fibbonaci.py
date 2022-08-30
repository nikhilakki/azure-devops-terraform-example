def create_fibbo_series(n: int):
    a = 1
    b = 1
    fib_series = [a, b]
    while a < n:
        c = a + b
        fib_series.append(c)
        a = b
        b = c
    return fib_series


def check_fibbo_num(n: int):
    fib_series = create_fibbo_series(n)
    if n in fib_series:
        return True
    else:
        return False


if __name__ == "__main__":
    n = input("Enter number: ")
    result = check_fibbo_num(int(n))
    print(f"{result}")
