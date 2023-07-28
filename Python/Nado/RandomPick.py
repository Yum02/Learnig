# 1. comment number is twenty, id is 1~20
# 2. random but not duplication
# 3. use random module, function stuffle(), sample()

from random import *

number = range(1, 21)
list = list(number)
shuffle(list)
prize = sample(list, 4)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(prize[0]))
print("커피 당첨자 : {}".format(prize[1:]))