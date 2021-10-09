'''
인덱스를 데리고 다니는 링크드 리스트인 deq를 정의하여
remove method 와 나머지 연산 활용
'''
from collections import deque
N = int(input())
ballons = list(map(int, input().split()))
deq = deque()
for i in range(N):
    deq.append((i+1,ballons[i]))

idx = 0
ans = []
while len(deq) != 1:
    n = deq[idx][1]
    size = len(deq)-1
    ans.append(deq[idx][0])
    deq.remove((deq[idx][0], n))

    if n > 0: n-= 1  
    idx = (idx+n) % size
ans.append(deq[0][0])
print(*ans)

