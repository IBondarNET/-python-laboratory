import re
"""Система:
 якщо х<=3, то x**2-3*x+9
 якщо х>3, то 1/(x**3+6)"""
re_float = re.compile("^-{0,1}\d{1,}\.{0,1}\d{0,}$")

def validator(pattern,promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

def validator2(prompt):
    number = float(validator(re_float,prompt))
    return number
q = 0
while q != "ex":
	x = validator2("х = ")

	res1 = (pow(x,2)-3*x+9)
	res2 = (1/(pow(x,3)+6))

	if x > 3:
		print("Функція дорівнює :" + str(res2))

	else :
		print("Функція дорівнює :" + str(res1))
	print("Робота програми завершена")
	q = input("Введіть <<ex>> для виходу з програми : ")