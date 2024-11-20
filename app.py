import math
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


def check(L,R,content):
    is_a = True
    for i in content:
        if i[0] >= L and i[1] <= R:
            is_a = False
    
    return is_a


N,M = in_i()
content = []
for i in range(N):
    L,R = in_i()
    content.append((L,R))

content = sorted(content)
ans = set()
for i in range(M):
    L,R = i+1,i+1
    for u in range(M-L+1):
        if check(L,R+u,content):
            ans.add((L,R+u))

print(len(ans))
