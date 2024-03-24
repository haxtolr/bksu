#슬라이싱 예제
## jumin = "990120 - 1234567"
##jumin = "990120-1234567"
##m = jumin[7]
##year = jumin[:2]
##mo = jumin[2:4]
##day = jumin[4:6]
##birth = jumin[:6]
##b = jumin[8:]
##ba = jumin[-7:]
##
##print(f"성별 {m}")
##print(f"년도 {year}")
##print(f"월 {mo}")
##print(f"일 {day}")
##print(f"생일 {birth}")
##print(f"뒷자리 {b}")
##print(f"뒷자리 {ba}")


##price = ['20180728', 100, 130, 140, 150, 160, 170]
##
##print(price[1:])
##
##num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
###print(num[0:9:2])
##print(num[::-1])
##print(num)

##corp = ["KG", "SAM", "LG", "SK", "ASET"]
##print("/".join(corp))
###print("\n".join(corp))
##
##s = '/'.join(corp)
##s = s.split('/')
##print(s)
##
## 리스트 정렬 sort()

##num = [10, 2, 1, 3, 4, 12, -13, 5, 9, 149]
##num.sort()
##print(num)
##na = sorted(num)
##print(na)
##
##
##ne = "http://daum.com"
##site = ne.replace("http://","")
##a = site.find('.')
##l = len(site[:a])
##c = site.count('e')
##pa = site[:3] + str(l) + str(c) + '!' 
##print(pa)
##
##sub1 = 10
##sub2 = 20
##sub3 = 30
##subway = ["유재석", "조새호", "박명수"]
##print(subway.index("조새호"))
##subway.append("하하") # 맨뒤 하하 추가
##subway.insert(1, "정현돈") # 정현동 1번 인덱스 추가
##print(subway.pop()) #뒤에서 하나 뺌
##print(subway.pop())
##subway.append("유재석")
##subway.count("유재석")

##num = [1, 2, 3, 4, 5, 6, 7]
##mix_list =["조세호", 30, True]
##num.extend(mix_list)
##print(num)

