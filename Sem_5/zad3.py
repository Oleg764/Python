#3. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
#имена str, ставка int, премия str с указанием процентов вида “10.25%”.
#В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
#Сумма рассчитывается как ставка умноженная на процент премии
Names =['Semen','Olga','Sergey','Svetlana']
Stavka = [34,34,23,67]
Persent = ['3%','4%','2.23%','5.08%']
for i,j,x in zip(Names, Stavka,Persent):print(f"Входные данные : {i}  {j}  {x} ")
def Persent_fl(Persent):

     Persent = [float(i.strip('%'))  for i in Persent]
     return Persent
def dict_rezult():
     dict1 = {k:v*p for k,v,p in zip(Names,Stavka,Persent_fl(Persent))}
     return dict1
print('Итоговый словарь :',dict_rezult())