print("Бондар Ілля Юрійович \nЛабораторна робота №1 \nВаріант 1 \nОбчислення функції")
print("KM - 93")

x = float(input("х = "))

res1 = (pow(x,2)-3*x+9)
res2 = (1/(pow(x,3)-6))

if x > 3:
	print("Функція дорівнює :" + str(res2))

else :
	print("Функція дорівнює :" + str(res1))
print("Робота програми завершена")