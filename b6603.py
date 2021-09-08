'''
dfs? 방문체크 리스트를 통한 재귀
'''
def dfs(i,N):
    if N == 6:
        for i in range(k):
            if v[i]:
                print(S[i], end=" ")
        print()
        return
    else:
        for j in range(i,k):
            if not v[j]:
                v[j] = 1
                dfs(j,N+1)
                v[j] = 0
k = 1
while k:
    k, *S = list(map(int, input().split()))
    v = [0]*k
    dfs(0,0)
    print()

# k = 1
# while(k):
#     k, *S = list(map(int, input().split()))
#     for i in range(1, 1<<k):
#         ans = []
#         for j in range(k):
#             if i & 1<<j:
#                 ans.append(S[j])
#         if len(ans) == 6:
#             print(*ans) 
#     print()
        

    


