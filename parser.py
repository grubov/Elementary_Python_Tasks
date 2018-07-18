##################################################################
## Файловый парсер
##   
## Нужно написать программу, которая будет иметь два режима:
## 1. Считать количество вхождений строки в текстовом файле. 
## 2. Делать замену строки на другую в указанном файле
##
##     Программа должна принимать аргументы на вход при запуске:
## 1. <путь к файлу> <строка для подсчёта>
## 2. <путь к файлу> <строка для поиска> <строка для замены>
##################################################################

import sys

flag_mode = None
count = 0

if len(sys.argv) == 3:
    print('Search mode')
    path = sys.argv[1]
    search_string = sys.argv[2]
    flag_mode = 1
elif len(sys.argv) == 4:
    print('Replace mode')
    path = sys.argv[1]
    old_string = sys.argv[2]
    new_string = sys.argv[3]
    flag_mode = 2
else:
    print("Usage: program.py [path] [search] [replace]")

if flag_mode == 1:
    try:
        f = open(path, 'r')
        l = [line for line in f]
        for arg in l:
            count = count + arg.count(search_string)
        print("Matches found: %d " % count)
        f.close()
    except OSError:
        print('File not found')

if flag_mode == 2:
    try:
        with open(path, 'r') as f:
            l = [line for line in f]
            for arg in l:
                count = count + arg.count(old_string)

            for i in range(len(l)):
                l[i] = l[i].replace(old_string, new_string)

        with open(path, 'w') as v:
            for line in l:
                v.write(line)
        print("Count of replace:", count)

    except OSError:
        print('File not found')
