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
data = []
for i in range(N):
    data.append(in_li())
    
p(data)

#初期化
result = -1
num = 0
for i in range(0,N-2):
    total = 0
    result_o = 0
    total_num = [0,0]
    for u in range(3):
        if i == result:
            continue
        else:
            result_o = i
        for z in range(3):
            if z == result_o:
                continue
            else:
                result_o = z
            for o in range(3):
                if o == result_o:
                    continue
                else:
                    total = max(total,data[i][u]+data[i+1][z]+data[i+2][o])
                    p(total)
                    if total < data[i][u]+data[i+1][z]+data[i+2][o]:
                        total_num = [data[i][u],u]

    num += total_num[0]
    result = total_num[1]
    
p(num)