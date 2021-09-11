'''
도시에 도착할 때마다 if문을 통해 최소 주유값인지 확인하여
갱신한뒤 거리를 곱하여 누적해감
'''
N = int(input())
L = list(map(int,input().split()))
costs = list(map(int,input().split()))

minc = costs[0]
tot = L[0]*minc
for i in range(1, N-1):

    if minc > costs[i]:
        minc = costs[i]

    tot += L[i]*minc

print(tot)        
