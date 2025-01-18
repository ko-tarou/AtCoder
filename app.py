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


def check(x,y,R):
    if (x+0.5)**2 + (y+0.5)**2 <= R**2:
        return True
    else:
        return False

#入力
R = int(input())

point = R
origin_x = 0
is_loop = True
total = 0
none_total = 0

while is_loop:
    x = origin_x
    y = 0

    for _ in range(point):
        if check(x,y,R):
            total += 1
            if y == 0:
                none_total += 1
            x += 1
            y += 1
        else:
            if y == 0:
                is_loop = False
            break
    
    if x == y:
        one = total

    point = y
    origin_x += 1


four = (total-one)*2+one
p((four-none_total)*4+1)