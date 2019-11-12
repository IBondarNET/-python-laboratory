"""Організація циклу за допомогою оператора while"""
""" Дано ціле число, що складається з різних цифр. 
Визначити, яка з цифр заданого числа більше, тобто знайти найбільшу цифру числа."""
import re
re_int = re.compile("^-{0,1}\d+$")
def validator(pattern,promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return (text)
q = 0
while q != "ex":
    x = validator(re_int,("x = "))
    i = 0
    c = len(x)
    buffer = 0
    while(i < c):
        compare = int(x[i])
        i += 1
        if compare > buffer :
            buffer = compare
    print(buffer)
    q = input("Введіть <<ex>> для виходу з програми : ")
