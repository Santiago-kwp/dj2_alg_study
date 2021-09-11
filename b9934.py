'''
완전 이진트리 인덱싱
start = 2**(K-i-1)-1
end = 2**K -1
step = 2**(K-i)
'''
K = int(input())
v = list(map(int, input().split()))

for i in range(K):
    for j in range(2**(K-i-1)-1,2**K-1,2**(K-i)):
        print(v[j], end=" ")
    print()