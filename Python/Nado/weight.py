# 1. man weight average is height(m) * height(m) * 22
# 2. woman weight average is height(m) * height(m) * 21
# 3. average weight is using function(function name is 'std_weight') and it use transfer value(height, gender)

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21
print("당신의 성별(남자 or 여자")
gender = str(input())
print("당신의 키(cm기준) : ")
height = int(input())
weight = round(std_weight(height / 100, gender), 2)

print(f"키 {height}cm {gender}의 표중 체중은 {weight}kg입니다.")