# #dictionary = {키1: 값1, 키2 : 값2, ...}
# lux = {
#     'health' : 490, 'mane' : 334, 'melee' : 550, 'armor' : 18.72
# }

# #키 자리에는 리스트 사용 X
# x = {100 : 'hunderd', False : 0,  3.5 : [3.5, 3.5]}

# #키 할당하기
# lux['health'] = 100
# print(lux['health'])

# #딕셔너리에 키가 있는지 확인
# print('health' in lux)

# #키 개수 구하기
# print(len(lux))

#심사문제
x = input().split()
y = map(float, input().split())
lux = dict(zip(x, y))
print(lux)