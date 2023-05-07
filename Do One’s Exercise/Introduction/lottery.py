from random import *

num_list = []
for i in range(6):
    a = randint(1, 46)
    while a in num_list:
        a = randint(1, 46)
num_list.append(a)

print(num_list)