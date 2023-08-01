# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.


__all__ = ['valid_year', 'leap_year']
def leap_year(year):
    if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
        return True


def valid_year(date):
    day, month, year = (int(item) for item in date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
        return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    if month == 2 and not leap_year(year) and day > 29:
        return False
    if month == 2 and leap_year(year) and day > 28:
        return False
    else:
        return True

if __name__=='__main__':
    print(valid_year('29.02.2029'))
