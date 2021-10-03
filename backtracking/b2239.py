'''
0이 아닌 숫자를 count 배열에 행, 열, 3x3 박스에 저장하고, 배정이 안된 숫자의 위치를 큐에 저장
큐를 하나씩 DFS를 통해 순회하면서 1부터 9까지 count 배열에 없는 숫자일 경우 해당 숫자를 입력하고
재귀를 통해 다음 위치로 이동, 만약 검사를 통과하지 못하면 돌아와서 다음 위치로 이동

'''
def dfs(n):
    i , j = Q[n]
    b = 3*(i//3)+(j//3)
    for k in range(1, 10):
        if not icnt[i][k] and not jcnt[j][k] and not bcnt[b][k]:
            icnt[i][k], jcnt[j][k], bcnt[b][k] = 1, 1, 1
            arr[i][j] = k
            if n == len(Q)-1:
                for i in range(9):
                    print(''.join(map(str, arr[i])))
                exit()
            dfs(n+1)
            icnt[i][k], jcnt[j][k], bcnt[b][k] = 0, 0, 0
            arr[i][j] = 0

arr = [list(map(int, input())) for _ in range(9)]
icnt, jcnt, bcnt = [[0]*10 for _ in range(9)], [[0]*10 for _ in range(9)], [[0]*10 for _ in range(9)]
Q = []
for i in range(9):
    for j in range(9):
        r = arr[i][j]
        if r:
            icnt[i][r] = 1
            jcnt[j][r] = 1
            bcnt[3*(i//3)+(j//3)][r] = 1
        else:
            Q.append((i, j))
dfs(0)