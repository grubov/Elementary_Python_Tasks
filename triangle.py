## Сортировка треугольников
##
## Разработать консольную программу, выполняющую вывод треугольников
## в порядке убывания их площади.
##
## После добавления каждого нового треугольника программа спрашивает,
## хочет ли пользователь добавить ещё один.
## Если пользователь ответит “y” или “yes” (без учёта регистра),
## программа попросит ввести данные для ещё одного треугольника,
## в противном случае – выводит результат в консоль.
## 
## Расчёт площади треугольника должен производится по формуле Герона.
## Каждый треугольник определяется именем и длинами его сторон. 
## Формат ввода (разделитель - запятая):
## <имя>, <длина стороны>, <длина стороны>, <длина стороны>
## Приложение должно обрабатывать ввод чисел с плавающей точкой.
## Ввод должен быть нечувствителен к регистру, пробелам, табам.
##
## Вывод данных должен быть следующем примере:
## ============= Triangles list: ===============
## 1. [Triangle first]: 17.23 сm
## 2. [Triangle 22]: 13 cm
## 3. [Triangle 1]: 1.5 cm


import math


def validation(n):
    try:
        number = float(n)
        if number > 0:
            return number
        else:
            raise ValueError
    except ValueError:
        print('Incorrect value, enter a number > 0')
        return 0


def triangle_is_exist(a, b, c):
    if (a + b) > c and (b + c) > a and (a + c) > b:
        return True


def triangle_is_valid(name, a, b, c):
    if a and b and c and name:
        if triangle_is_exist(a, b, c):
            return True


def continue_enter(answer):
    if (answer.lower() == 'y') or (answer.lower() == 'yes'):
        return True
    else:
        return False


class Triangle:
    """A triangle class"""

    def __init__(self, name, a, b, c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.s = self.area(a, b, c)

    def __lt__(self, other):
        return self.s < other.s

    def __str__(self):
        ##        return '[Triangle '+self.name+']: '+ str(self.s) + ' cm'
        return '[Triangle %s]: %.2f cm' % (self.name, self.s)

    def area(self, a, b, c):
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return s


if __name__ == "__main__":
    triangles = []
    while True:
        name = input("name=")
        a = input("side a=")
        a = validation(a)
        b = input("side b=")
        b = validation(b)
        c = input("side c=")
        c = validation(c)
        if triangle_is_valid(name, a, b, c):
            triangle = Triangle(name, a, b, c)
            triangles.append(triangle)
        answer = input('Do you want to add another triangle? [yes] / [no]: ')
        if not continue_enter(answer):
            break
    triangles.sort(reverse=True)
    print('============= Triangles list: ===============')
    for x in triangles:
        print(x)
