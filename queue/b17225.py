# A: 상민이(B)가 포장하는데 걸리는 시간
# B: 지수(R)가 포장하는데 걸리는 시간
# N: 손님 수

A, B, N = map(int, input().split())
times = []
for _ in range(N):
    t, c, m = input().split()
    t = int(t)
    m = int(m)

    if c == 'B':
        for _ in range(m):
            times+=[(t, t+A, 1)]
            t += A
    else:
        for _ in range(m):
            times+=[(t, t+B, 2)]
            t += B

tot = []
e1 = e2 = 0
An = Bn = 0
# 시작 시간을 기준, 시작 시간이 같다면 빨리 끝나는 순으로으로 오름 차순 정렬
for s, e, n in sorted(times, key=lambda x: (x[0], x[1])):
    if n == 1:
        An += 1
        if s >= e1:
            e1 = e
            tot += [(s, e, n)]
        else:
            tot += [(e1, e1+A, n)]
            e1 += A
    else:
        Bn += 1
        if s >= e2:
            e2 = e
            tot += [(s, e, n)]
        else:
            tot += [(e2, e2+B, n)]
            e2 += B


order = 1
Aans, Bans = [], []
for _, _, n in sorted(tot, key=lambda x:(x[0], x[2])):
    if n==1:
        Aans.append(order)
    else:
        Bans.append(order)
    order += 1

print(An)
print(*Aans)
print(Bn)
print(*Bans)

