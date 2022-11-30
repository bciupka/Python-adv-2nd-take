# coding=iso-8859-2


while True:
    option = input("Wybierz opcje 1, 2, 3\n")
    if option:
        break

options = ['load data', 'export data', 'analyze & predict']

try:
    number = int(option)
except:
    print("To nie numer tłuku")
try:
    print(options[number - 1])
except:
    print("Nie ten numer")