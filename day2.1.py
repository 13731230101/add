import random
cai=random.randint(0,150)
print(cai)
jinbi=5000
i=0
while i<10:
    num=input("请输入您猜的数字")
    num=int(num)
    if num<cai:
        jinbi-=500
        print("小了，您的金币还剩",jinbi)

    elif num>cai:
        jinbi-=500
        print("大了，您的金币还剩",jinbi)
    else:
        jinbi+=3000
        print("恭喜您猜中了，您的金币还剩",jinbi)
        break
    i=i+1