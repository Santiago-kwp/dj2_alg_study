N = int(input())
T = list(map(int,input().split()))
T.sort()
elapse = 0
for t in range(N):
    elapse += sum(T[:t+1])
print(elapse)