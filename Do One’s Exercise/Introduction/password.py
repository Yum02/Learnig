# make site password
# site = http://naver.com, http://daum.net, http://google.com, http://youtube.com
# 1. exclude word 'http://'
# 2. exclude word '.com'
# 3. Add the number of letters to the first three digits of the remaining letters. 
# 4. Add the number of e's in the letter and add '!'
# (example password : naver -> nav5!)

sitename = "http://naver.com"
password = sitename.replace("http://", "") # replace함수를 이용해 "http://"라는 문자를 ""와 같은 빈칸으로 바꿈
password = password.replace(".com", "")
# password = password[:password.index(".") # 11번 코드와 기능은 같음
password = password[:3] + str(len(password)) + str(password.count("e")) + "!"

print("{0}의 비밀번호는 {1}입니다.".format(sitename, password))