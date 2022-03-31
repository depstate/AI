#1
price_list=[32100,32150,32000,32500]
for i in range(len(price_list)):
    print("{} {}".format(i,price_list[i]))

#2
for i in range(1, 4):
    print(90 + 10 * i, price_list[i])

#3
for a in range(2002, 2051, 4) :
    print (a)

#4
for n in range(10):
    print(n/10)

#5
ticker="btc_krw"
b=ticker.upper()
print(b)

#6
file_name='보고서.xlsx'
x=file_name.endswith('xlsx')
print(x)

#7
c = "hello world"
print(c.split())

#8
date="2020-05-01"
print(date.split("-"))

#9
상장주식수 = "5,969,782,550"
d=int(상장주식수.replace(",",""))
print(d)
print(type(d))

#10
c = "hello world"
print(c.split())

#11
price=['20180728','100','130','140','150','160','170']
print(price[1:])

#12
nums=[1,2,3,4,5,6,7,8,9,10]
print(nums[1::2])

#13
리스트=[3,100,23,44,12]
for i in 리스트:
    if i%3==0:
        print(i)