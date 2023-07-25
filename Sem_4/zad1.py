#1.  Напишите функцию для транспонирования матрицы
a = [[4, 7, 8], [9, 2, 4], [3, 2, 8]]
s = [[5,6,7],[0,9,8],[4,2,9]]
# d = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
def transp(a) :
     print(" Исходная матрица : ", *a, sep='\n')
     d = []
     for j in range(len(a)):
             # d.append(a[j])
             b = []
             d.append(b)
             for i in range(len(a[0])):

                     b.append(a)
                     d[j][i] = a[i][j]
     return d
print("Транспонированная матрица :", *transp(a), sep='\n')