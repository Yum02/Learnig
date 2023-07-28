# 1. The time required is 5~50Min (time is random)
# 2. 5~15min ok, else time isn`t
# 3. matching -> [o] else []

from random import *
cnt = 0

for i in range(1, 51):
    time = randint(5, 50)
    if 5 <= time <= 15 :
        print(f"[0] {i}번째 손님 (소요시간 : {time}분)")
        cnt += 1
    else :
        print(f"[ ] {i}번째 손님 (소요시간 : {time}분)")

print(f"총 탑승객 : {cnt}")