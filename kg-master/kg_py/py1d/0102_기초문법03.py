###국 영 수 점수를 입력받아 합계/평균
##
##x = int(input("국어: "))
##y = int(input("영어: "))
##z = int(input("수학: "))
##
##a = x + y + z
##b = round(a / 3, 1)
##
##print(f"합계는 {a}이고, 평균은 {b}입니다.")


#문자열 인덱싱, 슬라이싱, 함수 count(), upper(), lower(), lstrip()

a = " hobBy      "
print(a.count('b'))
print(len(a))
print(a.upper())
print(a.lower())
print(a.lstrip())
print(a.rstrip())
print(a.strip())

#replace()

b = "Life is too short"

b.replace("Life", "leg")
print(b.replace("Life", "leg"))


#split()
c = b.split()
print(b.split())
