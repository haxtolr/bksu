movie = ["어벤져스", "럭키", "스파이더맨"] #리스트
print(movie)

movie.append("베트맨") #리스트 뒤에 추가
print(movie)

movie.insert(1,"범죄도시") #1번 인덱스 앞에 추가
print(movie)

del movie[2] # 2번 인데스 삭제
print(movie)

lang1 = ["A", "B", "C"]
lang2 = ["D", "E", "F"]
langs = lang1 +lang2
print(langs)

#리스트에서 최대 최솟값 출력

##num = [1, 2, 3, 4, 5, 6, 7, -10, 100]
##
##ma = max(num)
##mi = min(num)
##print(f"MAX : {ma}")
##print(f"min : {mi}")
##
##sr = ["apple", "del", "zhar", "lang", 1, 2, 3, 4]
##print("max : ", len(sr))
##

# num의 평균값

num = [1, 2, 3, 4, 5, 695, 592, 100, 3002, 10230, 1004]
a = sum(num) / len(num)
print("평균 : ", a)


