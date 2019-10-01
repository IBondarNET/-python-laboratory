import math
print("Бондар Ілля Юрійович \nЛабораторна робота №1 \nВаріант 1 \nПереведення радіанної міри кута")
print("KM - 93")

a = int(input("Вкажіть радіани :"))

res = float(math.degrees(a))

print("Градусів: " + str(round((res),3)))
print("Хвилин: " + str(round((res * 60),3)))
print("Секунд: " + str(round((res * 3600),3)))
print("Робота програми завершена")
