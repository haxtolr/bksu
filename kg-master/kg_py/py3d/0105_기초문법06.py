# # 실습 정수를 받아 결과값 구하기

# #n = input("n : ")
# #a = int(n) + int(n + n) + int(n + n + n)
# #print(a)

# # 동전으로 나눌 것


# i500 =  0
# i100 = 0
# i50 = 0
# i10 = 0

# n = int(input("금액 : "))

# i500 = n//500
# n = n%500
# i100 = n//100
# n = n%100
# i50 = n//50
# n = n%50
# i10 = n//10
# n = n%10

# print (f"500원 : {i500}, 100원: {i100}, 50원 : {i50}, 10원 : {i10}, 1원 : {n}")

# app1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
# app2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
# app3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.0]
# rating_sum = app3[4] + app1[4] + app2[4]
# rating_avg = rating_sum
# #코드작성하기-------------
# print(f"{app1[0]} rating : {app1[4]}")
# print(f"{app2[0]} rating : {app2[4]}")
# print(f"{app3[0]} rating : {app3[4]}")
# #------------------------
# print("rating average:", rating_avg)

# age = int(input("나이 : "))
# height = int(input("키 : "))
# if age >= 10 & height >= 110:
# 	print("놀이기구 가능")
# else:
# 	print("불가능")

# age = int(input("나이 : "))
# if age >= 65 or age <=7:
# 	print("free")
# elif age >= 8 and age <= 18:
# 	print("1000원")
# else:
# 	print("3000원")

# price = int(input("가격: "))
# if price >= 10000 and price < 50000:
# 	dis_price = (price//100*5)
# 	last_price = price - dis_price
# 	dis_rate = 5
# elif price >= 50000 and price < 100000:
# 	dis_price = (price//100*7.5)
# 	last_price = price - dis_price
# 	dis_rate = 7.5
# elif price >= 100000:
# 	dis_price = (price//100*10)
# 	last_price = price - dis_price
# 	dis_rate = 10
# else:
# 	dis_price = 0
# 	dis_rate = 0
# 	last_price = price
# print(f"구매가 : {price}")
# print(f"할인율 : {dis_rate}%")
# print(f"할인금액 : {int(dis_price)}원")
# print(f"지불금액 : {int(last_price)}원")

name = input("이름 : ")
hi = int(input("키 : ")) * 0.01
we = int(input("몸무게 : "))
bmi = round(we/(hi*hi), 1)
kg = round(21 * (hi*hi), 1) 

if bmi < 18.5:
	a = "저체중"
elif bmi >= 18.5 and bmi < 22.9:
	a = "정상"
elif bmi >= 23.0 and bmi < 24.9:
	a = "과체중"
elif bmi >= 18.5 and bmi < 29.9:
	a = "비만 1단계"
elif bmi >= 18.5 and bmi < 40.0:
	a = "비만 2단계"
elif bmi >= 40:
	a = "비만 3단계"

print(f"{name}님의 신체질량지수(BMI)는 {bmi}이며, {a}입니다.")
print(f"{name}님의 적정체중은 {kg}kg입니다.")
