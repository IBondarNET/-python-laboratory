import re
"""Організація циклу за допомогою оператора for"""
"""Обчислити ∑(from i=1 to n) (i*x)"""
re_int = re.compile("^\d+$")
re_int2 = re.compile("^-{0,1}\d+$")
def validator(pattern,promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return int(text)
q = 0
while q != "ex":
    n = validator(re_int,("n = "))
    x = validator(re_int2,("x = "))
    i = 1
    res = 0
    for i in range(1,n+1):
        res1 = i*x
        i += 1
        res += res1
    print(res)
    q = input("Введіть <<ex>> для виходу з програми : ")

