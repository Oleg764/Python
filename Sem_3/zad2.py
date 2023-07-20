#2. Дан список повторяющихся элементов.
#Вернуть список с дублирующимися элементами.
#В результирующем списке не должно быть дубликатов.
spisok_1 = [23,4,5,'a',156,23,54,2233,'a',17,156,5,98,43]
spisok_2 = []
print(spisok_1)
for i in spisok_1:
    if i  not in spisok_2:
        if spisok_1.count(i) != 1:
           spisok_2.append (i)
print(spisok_2)