



import random as rnd

n=8
count=0

x = [1,2,3,4,5,6,7,8]
def gen_positions():
    y = []
    for i in range(n):
        row = rnd.randint(1,8)

        y.append(row)
    return y
    print(f'координаты х {x}, координаты  у {y}')




while count != 4:
    y =  gen_positions()
                                    
    rezult = True
    for i in range(n):
        for j in range(i+1,n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):

                rezult = False


    if rezult :
        print('NO','ферзи не бьют друг друга ')
        print(f'координаты х {x}, координаты  у {y}')
        count+=1

