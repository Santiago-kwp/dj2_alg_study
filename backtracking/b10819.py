'''
정렬하여 min, max 값을 앞 뒤로 번갈아가며 넣어서 새로운 리스트를 만들어서 푸는 로직
'''
N = int(input())
a = sorted(list(map(int, input().split())))
newa = []
s, l, r = 0, 0, N-1
while (l<=r):
    if l == r:
        if abs(a[l]-newa[0]) > abs(a[l]-newa[-1]):
            newa.insert(0,a[l])
        else:
            newa.append(a[l])
    elif l%2:
        newa.append(a[l])
        newa.insert(0,a[r])
    else:
        newa.append(a[r])
        newa.insert(0,a[l])
    l += 1
    r -= 1

for i in range(N-1):
    s += (abs(newa[i]-newa[i+1]))

print(s)
# def f(i, cnt):
#     global maxn
#     if cnt < N:
#         sub = 0
#         for i in range(N-1):
#             sub += abs(a[i]-a[i+1])
#         if maxn < sub:
#             maxn = sub
#         else:
#             return
#     elif cnt == N:
#         sub = 0
#         for i in range(N-1):
#             sub += abs(a[i]-a[i+1])
#         return sub
#     else:
#         for j in range(i, N):
#             a[i], a[j] = a[j], a[i]
#             f(i, cnt+1)
#             a[i], a[j] = a[j], a[i]
# f(0,0) 
# print(maxn)
