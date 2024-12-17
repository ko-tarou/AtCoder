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
N = int(input())
A = []
S = []

for i in range(N):
    a,s = in_s()
    A.append(int(a))
    if s == "L":
        S.append(0)
    else:
        S.append(1)

#初期化
data = {0:-1,1:-1}
cost = 0

for i in range(N):
    rl = S[i]
    mark = A[i]
    if data[rl] == -1:
        data[rl] = mark
    else:
        cost += abs(data[rl]-mark)
        data[rl] = mark

print(cost)