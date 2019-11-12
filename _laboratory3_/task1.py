print("Бондар Ілля Юрійович \nЛабораторна робота №3 \nВаріант 1 \nПоміняти місцями слова з максимальною і мінімальною довжиною ")
while True:
    a = input("Введіть текст : ")
    b = a.split()
    i = 0
    resmax = 0
    resmin = len(b[i])
    rmx1 = 0
    rmn1 = 0
    maxcount = 0
    mincount = 0
    while i < len(b):
        a1 = b[i]
        res1 = len(a1)
        if resmax == res1:
            maxcount += 1
        elif resmin == res1:
            mincount += 1
        if resmax < res1:
            resmax = res1
            rmx1 = i
            maxcount = 1
        if resmin > res1:
            resmin = res1
            rmn1 = i
            mincount = 1
        i += 1
    if mincount == 1 & maxcount == 1:
        b[rmn1],b[rmx1] = b[rmx1],b[rmn1]
        print(' '.join(b))
    else :
        print("Помилка!!! \nУ вашому тексті слова з максимальною та\або мінімальною довжиною не є єдині!!! \nБудь ласка перевірте текст!)")
    print("Для виходу з програми , введіть \"y\" \nЩоб продовжить введіть будь що, крім \"y\"")
    exit = input("Вийти з програми ? :")
    if exit.lower() == "y":
        print("Робота програми закінчена, дякую!!!")
        break