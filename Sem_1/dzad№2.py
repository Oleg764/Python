#3. Напишите код, который запрашивает число и сообщает является ли оно простым
# или составным. Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
#num = int(input("Введите число :"))
while True:
    num = int(input("Введите число :"))
    if(num>0 and num < 100000):
        break
    else:
        print("Неправильный ввод , введите число больше нуля и меньше 100000  ")
i=2
while i<num:
    if (num%i!=0):
        i += 1
        if (i==num ):
            print("Число простое ")
    else:
        print("Число составное")
        break



