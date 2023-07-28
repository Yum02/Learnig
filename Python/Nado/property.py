class House:
    #위치, 건물 종류, 매물 종류, 가격, 준공연도
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    #매물 정보 표시
    def show_detail(self):
        print(f"{self.location} {self.house_type} {self.deal_type} {self.price} 원 {self.completion_year}년")

house = []
house1 = House("강남", "아파트", "매매", "10억", "2010")
house2 = House("마포", "오피스텔", "전세", "5억", "2007")
house3 = House("송파", "빌라", "월세", "500/50만", "2000")

house.append(house1)
house.append(house2)
house.append(house3)

print(f"총 {len(house)}가지 매물이 있습니다.")
for houses in house:
    houses.show_detail()

# class 강남(House):
#     def __init__(self):
#         House.__init__(self, "강남", "아파트", "매매", "10억", "2010")

# class 마포(House):
#     def __init__(self):
#         House.__init__(self, "송파", "오피스텔", "전세", "5억", "2007")

# class 송파(House):
#     def __init__(self):
#         House.__init__(self, "송파", "빌라", "월세", "500/50만", "2000")

# 강남.show_detail()