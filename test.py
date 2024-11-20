# 入力をリストにする
def in_li():
    return list(map(int, input().split()))

# 入力をそれぞれの変数にする
def in_i():
    return tuple(map(int, input().split()))

# リストを空白空けて返す
def out_list(data):
    return " ".join(map(str, data))

def total(num):
    return (num * (num + 1)) // 2

N, M = in_i()
X = in_li()
A = in_li()

sub = []
for i, u in zip(X, A):
    sub.append((i, u))

sub.sort()

if X[0] != 1 or X[-1] != N:
    print(-1)
    exit()

if sum(A) != N:
    print(-1)
    exit()

ans = total(N - 1)
count = 0
re = 1

for i, u in sub:
    diff = i - re
    count -= diff
    if count < 0:
        print(-1)
        exit()
    ans -= diff * (count - 1 + count - diff) // 2
    count += u
    re = i

if count != 1:
    print(-1)
    exit()

print(int(ans))
