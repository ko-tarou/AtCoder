import math

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


def check(L,R,content):
    is_a = True
    for i in content:
        if i[0] >= L and i[1] <= R:
            is_a = False
    
    return is_a


N,Q = in_i()
H = []
T = []
for i in range(Q):
    h,t = in_s()
    if h == "L":
        H.append(1)
    else:
        H.append(-1)
    T.append(int(t))



#初期化 L=1,R=-1
LR = { 1 : 1 , -1 : 2 }
total = 0
con = []

for i in range(Q):
    rl = H[i]
    data = LR[rl],T[i]
    data = sorted(data)
    
    con = []
    if not(data[1] > LR[rl*-1] and LR[rl*-1] > data[0]):
        con.append(data[1]-data[0])
    if not(LR[rl*-1] > data[1] or data[0] > LR[rl*-1]):
        con.append(N-data[1]+data[0])
        
    data = min(con)
    total += data
    LR[rl] = T[i]

print(total)