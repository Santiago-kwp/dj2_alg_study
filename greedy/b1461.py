# 풀이 방식 
# 1. +/- 양 방향으로 힙에 적재
# 2. 양수, 음수 집합의 개수를 M으로 나눴을 때 나머지가 있으면 나머지부터 힙에서 pop한 후 마지막 수 *2
# 3. M 으로 나눠 떨어지는 수만큼 힙에서 pop해서 마지막 수 * 2
# 4. 양의 최대값과 음의 최대값을 비교하여 더 큰 쪽 수를 total에서 뺌

import heapq
N, M = map(int, input().split())
loc = list(map(int, input().split()))
        
pos, neg = [], []
for x in loc:
    if x > 0:
        heapq.heappush(pos, x)
    else:
        heapq.heappush(neg,(-x, x))

total = maxD = 0
if pos:
    k, n = divmod(len(pos), M)
    if n:
        for _ in range(n):
            tmp = heapq.heappop(pos)
        total += 2*tmp
    for _ in range(k):
        for _ in range(M):
            tmp = heapq.heappop(pos)
        total += 2*tmp
    maxD = tmp
    
if neg:
    k, n = divmod(len(neg), M)
    if n:
        for _ in range(n):
            if neg:
                tmp = heapq.heappop(neg)[0]
        total += 2*tmp
    for _ in range(k):
        for _ in range(M):
            tmp = heapq.heappop(neg)[0]
        total += 2*tmp

total -= tmp if maxD < tmp else maxD
print(total)




