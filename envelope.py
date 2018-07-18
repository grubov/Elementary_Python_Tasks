exit='y'

def compare(a, b, c, d):
    if (a>c) and (b>d) or (a>d) and (v>c):
        print ("The envelop B can fit in the envelop A")
    else:
        print ("The envelop B can't fit in the envelop A")

while exit=='Y' or exit=='y':
    try:
        a = float(input("Envelop A width="))
        b = float(input("Envelop A height="))
        c = float(input("Envelop B width="))
        d = float(input("Envelop B height="))
    except (TypeError, ValueError):
        print('Incorrect value, enter a number')

    compare(a, b, c, d)
    exit=input ('Continue? Yes(y) / No(n)')
    exit.lower()