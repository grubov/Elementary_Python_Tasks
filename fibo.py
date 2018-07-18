def fibo_generator(max):
    a = b = 1
    for i in range(max):
        yield a
        a, b = b, a + b

def fibo(min, max):
    for i in fibo_generator(max):
        if max >= i >= min:
            print(i)

if __name__ == "__main__":
    try:
        min = int(input('min='))
        max = int(input('max='))
    except ValueError:
        print('Incorrect value, enter a number')

    fibo(min, max)


