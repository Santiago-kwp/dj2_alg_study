# 8! = 40320 이므로 모든 순열의 경우를 구해서 조건 만족 여부를 구하자
def perm(k):
    global cnt
    if k == len(A):
        w = 0
        for i in range(len(A)):
            w += A[i]-K
            if w < 0: return
        cnt += 1

    for i in range(k, len(A)):
        A[i], A[k] = A[k], A[i]
        perm(k+1)
        A[i], A[k] = A[k], A[i]

N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
perm(0)
print(cnt)