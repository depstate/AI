print('Hello World')

print("Mary's cosmetics")

print('신씨가 소리질렀다. "도둑이야".')

print('"C:\Windows"')

print("안녕하세요\n 만나서\t\t반갑습니다")  # \n은 줄바꿈 \t는 tab키 한칸 띄울때 사용

movie_rank=['닥터 스트레인지','스플릿','럭키']
print(movie_rank)

movie_rank.append("배트맨")
print(movie_rank)

movie_rank.insert(1,"슈퍼맨")
print(movie_rank)

nums=[1,2,3,4,5]
result=sum(nums)
print(result)

cook=["피자","김밥","만두","양념치킨","족발","피자","김치만두","쫄면","소시지","라면","팥빙수","김치전"]
print("cook 리스트의 데이터 개수 : ",len(cook))

nums=[1,2,3,4,5]
result=sum(nums)
print(result/len(nums))

print(3==5)  #3과 5는 같지 않다 F

print(3<5)   #3보다 5가 크다 T

x=4
print(1<x<5)     # x는 1과 5 사이에 있다 T

print((3==3)and(4!=3))   # 3=3이고, 4는 3이 아니다, and니까 둘다 참이여야 T이다