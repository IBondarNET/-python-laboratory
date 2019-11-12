import re
"""Увести з клавіатури три дійсних числа. 
Піднести до квадрата ті з них, значення яких невід'ємні, і в четверту ступінь - від`ємні ."""


re_float = re.compile("^-{0,1}\d{1,}\.{0,1}\d{0,}$")

def validator(pattern,promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

def validator2(prompt):
	number = float(validator(re_float,prompt))
	return number

a = validator2("Перше число = ")
b = validator2("Друге число = ")
c = validator2("Третє число = ")

if a >= 0:
	print("Результат для першого число : " + str(round(a**2,3)))
elif a < 0:
	print("Результат для першого число : " + str(round(a**4,3)))
if b >= 0:
	print("Результат для другого число : " + str(round(b**2,3)))
elif b < 0:
	print("Результат для другого число : " + str(round(b**4,3)))
if c >= 0:
	print("Результат для третього число : " + str(round(c**2,3)))
elif c < 0:
	print("Результат для третього число : " + str(round(c**4,3)))
print("Робота програми завершена")