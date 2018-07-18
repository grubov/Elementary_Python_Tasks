def fibo(max):
    a = b = 1
    for i in range(max):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    try:
        min = int(input('min='))
        max = int(input('max='))
    except ValueError:
        print('Incorrect value, enter a number')

    for i in fibo(max):
        if max >= i >= min:
            print(i)
