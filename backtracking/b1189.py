'''
방문하고, 리턴되서 돌아왔을 때 방문여부를 풀어주면서
추가 경로 탐색하는 기본적인 백트래킹 방법 활용
'''
d = [0, 0, -1, 1]
def backtrack(i, j, dst):
    global case
    if (i, j, dst) == (0, C-1, K):
        case += 1
        return
    if dst >= K: return
    for k in range(4):
        ni, nj = i+d[k], j+d[k-2]
        if ni in range(R) and nj in range(C):
            if not visited[ni][nj] and arr[ni][nj] == '.':
                visited[ni][nj] = 1
                backtrack(ni, nj, dst+1)
                visited[ni][nj] = 0

R, C, K = map(int, input().split())
arr = [input() for _ in range(R)]
visited = [[0]*C for _ in range(R)]
case = 0
visited[R-1][0] = 1
backtrack(R-1, 0, 1)

print(case)


