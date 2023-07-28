class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1


while True:
    try:
        print(f"[남은 치킨 : {chicken}]")
        order = int(input("치킨을 몇 마리 주문하시겠습니까? "))
        if order > chicken:
            print("재료 부족!")
        elif order <= 0:
            raise ValueError
        else:
            print(f"[대기번호 : {waiting}] {order}마리를 주문했습니다.")
            waiting += 1
            chicken -= order
            
        if chicken == 0:
            raise SoldOutError("치킨 소진")
    except ValueError:
        print("값을 잘못 입력했습니다.")

    except SoldOutError:
        print("재료가 소진돼 더이상 주문을 받지 않겠습니다.")
        break