import math
from itertools import product
import copy

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
    return " ".join(map(str,data))

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

def check(S):
    is_a = False
    val = (len(S)+1)//2-1
    if S[val] == "/":
        if S[0:val] == "1"*val:
            if S[val+1:len(S)] == "2"*val:
                is_a = True
    return is_a

#入力
N = int(input())
K = in_li()
K = sorted(K,reverse=True)

total = sum(K)
target = total//2
n = len(K)

dp = [False] * (target + 1)
dp[0] = True
for i in K:
    for u in range(target,i-1,-1):
        dp[u] = dp[u] or dp[u-i]

