import random
import os
def bomb():
    n=random.randint(0,280)
    d=0
    mi=0
    ma=280
    print("0~280")
    while(d!=n):
        d=int(input())
        print()
        if(d>mi and d<ma):
            if(d<n):
                print(d,"~",ma)
                print()
                mi=d
            elif(d>n):
                print(mi,"~",d)
                print()
                ma=d
            else:
                print("BOMB! ! !")
                print()
        else:
            print("请重新输入一个",mi,"~",ma,"之间的数")
            print()
def real():
    with open('real.txt') as f:
        datalist=f.readlines()
    with open('real.txt') as f:
        c=len(f.readlines())
    r=random.randint(0,c-1)
    print(datalist[r])
while 1:
    print("1. 数字炸弹")
    print("2. 真心话")
    print("其它任意键退出")
    print()
    a=input()
    print()
    if(a=='1'):
        bomb()
    elif(a=='2'):
        real()
    else:
        break
