import math
from itertools import product
import copy
import numpy as np

#print
def p(n):
    print(n)

#入力をリストにする
def in_li():
    return list(map(int,input().split()))

#入力をリストにする(文字)
def in_ls():
    return list(map(str,input().split()))

#入力をそれぞれの変数にする
def in_i():
    data = list(map(int,input().split()))
    return tuple(data)

#入力をそれぞれの変数にする(文字)
def in_s():
    data = list(map(str,input().split()))
    return tuple(data)

#リストを空白空けて返す
def out_list(data):
    print(" ".join(map(str,data)))

#0からnumまでindexをループさせる
def loop(index,num):
    if index == num:
        return 0
    else:
        return index+1
    
def total(num):
    return (num**2+num)/2

#n以上のmod(a) = bになる最小の数
def mod_min(n,a,b):
    if b >= a:
        return None
    
    k = math.ceil((n - b) / a)
    return k * a + b


#入力
L,R = in_i()
top = int(str(L)[0])
fin_top = int(str(R)[0])
length = len(str(L))
fin_length = len(str(R))
key = True
total = 0

while(key):
	total += (top)**(length-1)

	if top == fin_top and length == fin_length:
		key = False

	top += 1
	if top == 10:
		top = 1
		length += 1

p(total)

#一回目の調整
top = int(str(L)[0])
length = len(str(L))

data = str(top)
for i in range(length-1):
    data += str(top-1)

if L < int(data):
	total -= L - top*(10**(length-1))
else:
    p(data)
    p(top*(10**(length-1)))
    total -= int(data) - top*(10**(length-1))

p(total)

#二回目の調整
fin_top = int(str(R)[0])
fin_length = len(str(R))

data = str(fin_top)
for i in range(fin_length-1):
	data += str(fin_top-1)

if R < int(data):
	total -= int(data) - R

print(total)