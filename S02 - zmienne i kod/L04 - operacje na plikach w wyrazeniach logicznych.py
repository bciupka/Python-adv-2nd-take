# coding=windows-1250
import os
path = r"D:\Projekty\Kursy Python\Python - Advanced - VS\S02 - zmienne i kod\PLIKI\za oknem.txt"

def counting(path):
    with open(path, 'r') as f:
        text = f.read()
        splitted = text.split()

    lenght = len(splitted)
    print(text, splitted, lenght)
    return True


if os.path.isfile(path):
    counting(path)
else:
    print("Nie ma pliku")

os.path.isfile(path) and counting(path) or print('Nie ma pliku2')

print("łąka")