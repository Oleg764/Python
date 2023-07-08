#Напишите программу, которая запрашивает год и проверяет его на високосность.
#Распишите все возможные проверки в цепочке elif
#Откажитесь от магических чисел
#Обязательно учтите год ввода Григорианского календаря
#В коде должны быть один input и один print


year = int( input("Введите год ="))
if ( year < 1582 and year % 4 == 0 ):

    print("Год високосный")
elif (year % 4 == 0 and year % 100 != 0 and year >= 1582) or year % 400 == 0:
    print("Год високосный")

else:
    print("Год не високосный")