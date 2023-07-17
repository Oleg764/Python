#2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
#Функцию hex используйте для проверки своего результата.
num = int(input ("Введите число :"))
cel=(num//16)
ost = (num % 16)
if 0<ost<10:
    ost=str(ost)
elif  ost==10:
    ost=str("A")
elif  ost==11:
    ost=str("B")
elif  ost==12:
    ost=str("C")
elif  ost==13:
    ost=str("D")
elif  ost==14:
    ost=str("E")
elif  ost==15:
    ost=str("F")
num16=str(cel) + str(ost)
print(f"В шестнадцатеричной системе исчисления {num} ,будет =  {num16}")
print(f"Проверка с помощью hex = {hex(num)} ")