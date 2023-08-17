age = int(input())
balance = 9000

if 7 <=age<=12:
    print('삐빅! 어린이 요금입니다.\n650원')
    balnce = balance - 650
elif 13<= age < 18:
    print('삐빅! 청소년 요금입니다.\n1,050원')
    balnce = balance - 1050
else:
    print('삐빅! 어른 요금입니다.\n1,250원')
    balance = balance - 1250

print(f'잔액 : {balance}')
