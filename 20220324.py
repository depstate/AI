#1
letters='python'
print(letters[0],letters[2])

#2
string="PYTHON"
print(string[::-1])

#3
url=input("url : " )
domain=url.split('.')
print(domain[-1])

#4
file_name='보고서.xlsx'
x=file_name.endswith('xlsx')
print(x)

#5
file_name='2020_보고서.xlsx'
y=file_name.startswith('2020')
print(y)

#6
score=int(input("score : "))

if 100>=score>=81: print("A")
elif 80>=score>=61: print("B")
elif 60>=score>=41: print("C")
elif 40>=score>=21: print("D")
elif 20>=score>=0: print("E")

#7
cook=["피자","김밥","양념치킨","족발","피자","김치만두","쫄면","소시지","팥빙수","김치전"]
print(len(cook))

#8
warn_investment_list=["Microsoft","Google","Naver","Kakao","SAMSUNG","LG"]
a=input("종목명 : ")
if a in warn_investment_list: print("투자 경고 종목입니다")
else : print("투자 경고 종목이 아닙니다")

#9
list=[100,110,120]
for z in list:
    print(z+10)

#10
list2=["SK하이닉스","삼성전자","LG전자"]
for b in list2:
    print(len(b))
