



import random as rnd
x = []
y = []
n=8

def gen_positions(x,y):
    for i in range(n):
        x.append(rnd.randint(0, n - 1))
        y.append(rnd.randint(0, n - 1))
    return x, y

x,y=gen_positions(x,y)
print(f'координаты х {x}, координаты  у {y}')
correct = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            rezult = False

if rezult:
    print('NO','ферзи не бьют друг друга ')
else:
    print('YES,', 'ферзи  бьют друг друга')
