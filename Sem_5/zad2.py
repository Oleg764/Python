#2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
#Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
data=input("Введите абсолютный путь к файлу :")
def data_split(data):

    f=data.rsplit("/",1)

    f1=f[1].rsplit(".",1)

    print("Путь к файлу :  ",f[0]+'/', "; Имя файла : ", f1[0],"; Расширение файла :",f1[1])

print(data_split(data))


