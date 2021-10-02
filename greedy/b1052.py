'''
필요한 물병의 수는 이진수일 때 1의 개수
'''
N, K = map(int, input().split())
ans = 0
while bin(N).count('1') > K:
    N += 1
    ans += 1
print(ans)