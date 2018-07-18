##############################################################################################################################################
## Счастливые билеты.
##
## Есть 2 способа подсчёта счастливых билетов:
## 1. Московский — если на автобусном билете напечатано шестизначное число, и сумма первых трёх цифр равна сумме последних трёх,
## то этот билет считается счастливым.
## 2. Ленинградский, или Питерский — если сумма чётных цифр билета равна сумме нечётных цифр билета, то билет считается счастливым.
##
## Задача:
## Номер билета - шестизначное число. Нужно написать консольное приложение, которое может посчитать количество счастливых билетов.
## Для выбора алгоритма подсчёта читается текстовый файл. Путь к текстовому файлу задаётся в консоли после запуска программы.
##
## Индикаторы алгоритмов:
## 1 - слово 'Moskow'
## 2 - слово 'Piter'
## После задания всех необходимых параметров, программа в консоль должна вывести количество счастливых билетов для указанного способа подсчёта.
##############################################################################################################################################

import math
import sys
import time

count = 0


def selector(path):
    try:
        with open(path, 'r') as f:
            line = f.readline()
            if line=='1':
                return 1
            elif line=='2':
                return 2
            else:
                raise ValueError
                return 0
    except ValueError:
        print('File has an incorrect format' )
    except OSError:
        print('File not found')

def moscow(x):
    num1 = x // 1000
    num2 = x % 1000
    sum1 = num1 // 100 + ((num1 // 10) % 10) + num1 % 10
    sum2 = num2 // 100 + ((num2 // 10) % 10) + num2 % 10
    if sum1 == sum2:
        return True


def piter(x):
    sum1 = 0
    sum2 = 0
    odd = True
    while x > 0:
        if odd:
            sum1 = sum1 + x % 10
        else:
            sum2 = sum2 + x % 10
        x = x // 10
        odd = not odd
    if sum1 == sum2:
        return True

if __name__ == "__main__":
    sel=selector('ticket.txt')
    if sel == 1:
        print('Selected method: moscow')
        for x in range(0, 999999):
            if moscow(x):
                count = count + 1
    elif sel == 2:
        print('Selected method: piter')
        for x in range(0, 999999):
            if piter(x):
                count = count + 1

    print('Count of happy tcket:', count)


##while 1:
##    f3=piter(int(input("c=")))
##    print(f3)
