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
A = in_li()

#初期化
result_1 = 0
result_2 = 0
dp = [0]*N

for i in range(N):
    mark = A[i]
    if result_2 == 0:
        result_2 = mark
        dp[i] = 1
    elif result_1 == 0:
        result_1 = result_2
        result_2 = mark
        dp[i] = 2
    else:
        if(result_2-result_1 == mark - result_2):
            dp[i] = dp[i-1]+1
        else:
            dp[i] = 2
            
        result_1 = result_2
        result_2 = mark

print(sum(dp))
