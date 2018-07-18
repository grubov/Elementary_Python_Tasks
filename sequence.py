##################################################################
## Числовая последовательность
##
## Программа выводит ряд натуральных чисел через запятую,
## квадрат которых меньше заданного n.
## Программа запускается через вызов главного класса с параметрами.
##################################################################


def validation(n):
    try:
        number = int(n)
        if number:
            return number
        else:
            raise ValueError
    except ValueError:
        print('Incorrect value, enter a number')
        return 0


class Sequence:
    """A sequence class"""

    def __init__(self, limit):
        self.seq_list = []
        self.limit = limit

    def seq(self):
        for n in range(self.limit):
            if (n * n) < self.limit:
                self.seq_list.append(n)
        for x in self.seq_list:
            print( x, end=", ")



if __name__ == "__main__":
    limit = input("limit=")
    limit = validation(limit)
    sequence = Sequence(limit)
    sequence.seq()
