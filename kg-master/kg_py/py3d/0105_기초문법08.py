# num = 0
# while num < 10:
# 	num = num + 1
# 	if num % 2 == 1:
# 		continue
# 	print(num)

# #업다운 게임
# import random

# num = random.randint(1, 100)
# while 1:
# 	an = int(input("정답 : "))
# 	if an == num:
# 		print(f"정답 : {num}!")
# 		break
# 	elif an < num:
# 		print("업")
# 	elif an > num:
# 		print("다운")

# try:
# 	num = int(input("10을 나눌 숫자를 입력"))
# 	result = 10 / num
# 	print("Result : ", result)
# except ZeroDivisionError:
# 	print("오류 0으로 나눌 수 없습니다.")
# except ValueError:
# 	print("오류 : 유요한 정수를 입력하세요")

try:
	while 1:
		print("hi")
except KeyboardInterrupt:
	print("프로그램을 빠져나감니다.")