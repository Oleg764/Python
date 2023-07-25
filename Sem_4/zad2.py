#2. Напишите функцию принимающую на вход только ключевые
#параметры и возвращающую словарь, где ключ — значение
#переданного аргумента, а значение — имя аргумента. Если
#ключ не хешируем, используйте его строковое представление.

def my_func(**kwargs):  
    result = dict()
    for k, v in dict1.items():
        if v.__hash__ is True:
            
            result[v] = k
        else:
            result[str(v)] = k

    return result
dict1 = dict(first="one", second=2, third=3, fourth="four", fifth=[2, 3])
print(f"Исходный словарь :  {dict1} \nИтоговый словарь : {my_func()}")
