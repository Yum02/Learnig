# 심사문제
A, B, C, D, E = map(int, input().split())

if 0<= A <= 100 & 0<= B <= 100 & 0<= C <= 100 & 0<= D <= 100 & 0<= E <= 100:
    if A+B+C+D+E/5 >= 80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')
    
