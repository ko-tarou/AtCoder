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
rl = 1
result_1 = 0
result_2 = 0
dp = [0]*N

for i in range(N):
    mark = A[i]
    if result_2 == 0:
        result_2 = mark
        dp[i] = mark
        rl = rl * -1
    elif result_1 == 0:
        result_1 = result_2
        result_2 = mark
        dp[i] = mark
        rl = rl * -1
    else:
        if rl == 1 and result_2*2+mark < mark * 2:
                result_2 = mark
                if dp[i-1] > dp[i-2]:
                    dp[i-2] = 0
                else:
                    dp[i-1] = 0
                dp[i] = mark
        else:
            result_1 = result_2
            result_2 = mark
            dp[i] = mark
            rl = rl * -1
            

combo = 0
for i in range(N):
    if dp[i] == 0:
        if combo == 1:
            dp[i] = A[i]
            dp[i-1] = A[i-1]
        else:
            combo = 1
    else:
        combo = 0

rl = 1
ans = 0
for i in dp:
    if i == 0:
        continue
    elif rl == 1:
        ans += i
    else:
        ans += i*2
    rl = rl*-1

print(dp)
print(ans)