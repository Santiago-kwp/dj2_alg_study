'''
1, 3, 4, 2 => 3,4는 정렬되어 있고 2를 위로 -> 1을 위로
뒤에서 부터 하나씩 N과 비교하며 
1. 다른 경우, 즉 정렬이 안된 경우위로 옮겨야 되는 원소이고 
2. 같은 경우, 즉 정렬이 된 경우 N-- 하고 반복해서 찾아나감
정렬이 된 원소를 찾을 수록 N 이 줄어드는 구조
'''
import sys
N = int(input())
books = [int(sys.stdin.readline())]
for i in range(1,N):
    books.append(int(sys.stdin.readline()))

for book in books[::-1]:
    if book == N:
        N-=1
print(N)


