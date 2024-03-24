###딕셔너리
##cabinet = {3:"유재석", 100:"김태호"}
##
##print(cabinet[3])
##print(cabinet.get(3))
##print(cabinet.get(5, "사용가능"))
##print(5 in cabinet)
##
##del cabinet[3]
##cabinet[10] = "김종국"
##cabinet[5] = "송지효"
##print(cabinet)
##print(cabinet.keys())
##print(cabinet.values())
##print(cabinet.items())
##
##cabinet.clear()
##
###조건문
##result = 10 > 4
##
##if result:
##    print("test")
##
##result = 10 - 4
##if result:
##    print("hi")
##
##result1 = 10 > 4
##result2 = False
##result3 = result1 and result2
##if result3:
##    print("this is and")
##result3 = result1 or result2
##if result3:
##    print("this is or")
###조건문 퀴즈
##num = int(input("num : "))
##re = num % 2
##if re:
##    print("홀")
##else :
##    print("짝")
##

# 3 ~ 8사이의 숫자를 입력받아 해당 숫자를 꼭짓점으로 갖는 다각형 그리기
##import turtle
##
##num = int(input("num : "))
##t = turtle.Turtle()
##if num < 24 & num > 2:
##    print("error")
##else:
##    for i in range(num):
##        t.fd(25)
##        t.left(360/num)

#날씨를 입력받고 비 미세먼지 등을 입력받고
#해당 날씨에 비라면 우산을 챙기고
#미세먼지라면 마스크를 챙기세요
#아무것도 없으면 준비물 필요 없어요;

we = input("오늘 날씨는 : ")
if we == '비':
    print("우산을 챙기세요")
elif we == '미세먼지':
    print("마스크를 챙기세여")
else:
    print("준비물이 필요 없습니다.")










