sum = 0
count =0
while True:
    if sum > 5000000:
        sum = sum - 10 * sum / 100
        print("Ваша сумма превысила 5000000, с вас взимается налог на богатство 10 % , остаток  =", sum)
    print('''меню:1) Пополнить  
     2) Снять  
     3) Выйти ''')
    menu = int(input("Выберите пункт меню :"))
    if menu == 1:
       percent2 = 3*sum/100
       k = int(input("Введите сумму пополнения ,кратную 50 :"))
       if (k % 50 == 0):
          sum = sum + k
          print("На вашем депозите  ", sum)
          count+=1
          if count % 3 == 0:
               sum = sum + percent2
               print("Вы провели 3 операции снять/пополнить ,поэтому вам будет начислено 3% с суммы счёта : ",percent2," Общая сумма  :",sum)
    elif menu == 2:
        percent2 = 3 * sum / 100
        f = int(input("Введите сумму снятия ,кратную 50 :"))
        percent = f * 1.5 / 100
        if (f % 50 == 0 and f<=sum):
            sum = sum - f
            if ( percent >=30 and percent < 600):
                sum = sum - percent
                print("На вашем депозите  ", sum,"процент за снятие :",percent)
                count+=1
            elif percent <30:
                sum = sum-30
                count += 1
                if count % 3 == 0:
                    sum = sum + percent2
                    print("За 3 операции снять/пополнить  вам будет начислено 3% с суммы счёта :",percent2," Общая сумма = ",sum)
                print("На вашем депозите  ", sum,"процент за снятие :",percent)
            elif percent >600:
                sum = sum -600
                count += 1
                if count % 3 == 0:
                    sum = sum + percent2
                    print("За 3 операции снять/пополнить , вам будет начислено 3% с суммы счёта ",percent2," Общая сумма = ",sum)
                print("На вашем депозите  ", sum,"процент за снятие :",percent)
        else:
            print("Не достаточно средств")
    elif menu == 3:
        break

    elif sum > 5000000:
          sum = sum -  sum / 10
          print("Ваша сумма превысила 5000000, с вас взимается налог на богатство 10 % , остаток  =", sum)
