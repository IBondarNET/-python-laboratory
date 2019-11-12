import re
import math
'''Скласти програму переведення радіанної міри кута в градуси, хвилини і секунди.'''

re_int = re.compile("^[-+]{0,1}\d+$")

def validator(pattern,promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

q = 0
while q != "ex":
    res = math.degrees(float(validator(re_int,"Вкажіть радіани :")))
    print('Градусів: '  + str(round((res),3)))
    print('Хвилин:'  + str(round((res * 60),3)))
    print('Секунд: ' + str(round((res * 3600),3)))
    print('Робота програми завершена')
    q = input("Введіть <<ex>> для виходу з програми : ")


