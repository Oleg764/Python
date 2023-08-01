
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.



from sys import argv
def leap_year(year):
    if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
        return True


def valid_year(date):
    false = ('Дата не возможна')
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

if __name__ == '__main__':
   if  valid_year(argv[1]):
         print("Дата существует.")
   else:
        print("Дата невозможна.")
