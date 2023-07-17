from fractions import Fraction
f1 = str(input("Введите первое дробное число вида а/в :"))
f2 = str(input("Введите первое дробное число вида а/в :"))

a1 = int (f1[0])
a2 = int (f2[0])
b1 = int (f1[2])
b2 = int (f2[2])
#nt b
#nt c  = (a1*a2)
count = 1
while True:

    if ((a1*a2)%count == 0 and (b1*b2)%count == 0):
        a1 * a2 == a1* a2/count
        b1 * b2 == b1 * b2/count
        count+=1
        b = str(b1 * b2)
        c = str(a1 * a2)
    else:
        break


a = str(a1*b2 + a2*b1)
#b= str(b1*b2)
#c= str(a1*a2)
print("Сумма дробей = ",a + '/'+ b)
print("Произведение дробей = ",c + '/'+ b)
print("Проверяем с помощью модуля Fracthion: ","Сумма =",Fraction (a1,b1) +  Fraction (a2,b2),
      "; Произведение =",Fraction (a1,b1) * Fraction (a2,b2))
