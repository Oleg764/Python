from fractions import Fraction

f1 = str(input("Введите первое дробное число вида а/в :"))
f2 = str(input("Введите первое дробное число вида а/в :"))
a1,a2 = f1.split("/")
a1,a2 = int (a1),int(a2)
b1,b2 = f2.split("/")
b1,b2 = int (b1),int(b2)
b = b1 * b2
c = a1 * a2
a = (a1*b2 + a2*b1)
def cuts(n, m):
    if n > m:
        count = n
    else:
        count = m
    while count >1:
        if n % count == 0 and m % count == 0:
            n = n/count
            m = m/count
        else:
            count -= 1
    return n,m
print("Сумма дробей = ",cuts(a,b)[0] ,'/', cuts(a,b)[1])
print("Произведение дробей = ",cuts(c,b)[0],'/',cuts(c,b)[1])
print("Проверяем с помощью модуля Fracthion: ","Сумма =",Fraction (a1,b1) +  Fraction (a2,b2),
      "; Произведение =",Fraction (a1,b1) * Fraction (a2,b2))
