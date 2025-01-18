import math
from itertools import product
import copy
import numpy as np
from collections import deque

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
Q = int(input())

query= deque()
prefix = [0]
memory = 0


for i in range(Q):
    data = input()
    num = int(data[0])
    if num == 1:
        l = int(data[2:])
        query.append(l)
        prefix.append(prefix[-1]+l)
    
    if num == 2:
        memory += 1
    
    if num == 3:
        l = int(data[2:])
        p(prefix[l+memory-1]-prefix[memory])