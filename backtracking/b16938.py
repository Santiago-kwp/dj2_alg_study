'''
부분집합을 만들면서 조건에 부합하도록 만들기
가지치기 조건을 너무 빡빡하게 만들면 이후 가능성 있는 부분집합이 배제되버려서
합이 R보다 클 때만 가지치기를 적용해서 결과를 도출하였습니다.
'''
def backtrack(k, s, maxp, minp, diff):
    global way
    # 가지치기 L조건과 diff 조건의 경우 가지를 치면 이후 될 수 있는 집합이 날아가 버릴 수 있음
    if s > R: return
    if k == len(A):
        if s>=L and diff >=X: way += 1
        return
    MM, NN = max(maxp, A[k]), min(minp, A[k])
    backtrack(k+1, s+A[k], MM, NN, MM-NN)
    backtrack(k+1, s, maxp, minp, diff)

N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))
way = 0
backtrack(0, 0, 0, 1000001, 0)
print(way)