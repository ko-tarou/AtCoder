n, m = map(int, input().split())
x = list(map(int, input().split()))
a = list(map(int, input().split()))
p = [(0, 0)] * m
for i in range(m):
    p[i] = (x[i] - 1, a[i])
p.sort()
for i in range(m):
    x[i] = p[i][0]
    a[i] = p[i][1]
if x[m - 1] != n - 1:
    m += 1
    x.append(n - 1)
    a.append(0)

if x[0] != 0:
    print(-1)
    exit()

result = 0
for i in range(1, m):
    diff = x[i] - x[i - 1]
    if a[i - 1] < diff:
        print(-1)
        exit()
    result += diff * (a[i - 1] - 1 + a[i - 1] - diff) // 2
    a[i] += a[i - 1] - diff

if a[m - 1] != 1:
    print(-1)
    exit()

print(result)