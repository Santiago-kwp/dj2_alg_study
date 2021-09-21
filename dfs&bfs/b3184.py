# 아래 코드에서 중복을 최대한 줄여서 리펙토링
R, C = map(int, input().split())
field = [list(input()) for _ in range(R)]
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
def dfs(stack, o, v):
    while(stack):
        i, j = stack.pop()
        if field[i][j] == 'o':
            o += 1
        if field[i][j] == 'v':
            v += 1
        field[i][j] = '#'
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<R and 0<=nj<C and field[ni][nj] != '#':
                stack.append([ni,nj])
    return (o, 0) if o > v else (0, v)

ans = [0,0]
for r in range(R):
    for c in range(C):
        if field[r][c] != '#':
            o, v = dfs([[r,c]],0,0)
            ans[0] += o
            ans[1] += v

print(*ans)

# 지나온 길을 '#'을 통해 막으면서 while문과 stack을 통해 깊이 우선탐색
# R, C = map(int, input().split())
# field = [list(input()) for _ in range(R)]
# di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

# def dfs(start):
#     s = w = 0
#     while start:
#         i, j = start.pop()
#         if field[i][j] == 'o':
#             s += 1
#         if field[i][j] == 'v':
#             w += 1     
#         field[i][j] = '#'
   
#         for k in range(4):
#             ni, nj = i+di[k], j+dj[k]
#             if 0<=ni<R and 0<=nj<C:
#                 if field[ni][nj] != '#':
#                     if field[ni][nj] == 'o':
#                         s += 1
#                     if field[ni][nj] == 'v':
#                         w += 1          
#                     field[ni][nj] = '#'
#                     start.append([ni, nj])       
#     if s > w:
#         return s, 0
#     else:
#         return 0, w
# ans = [0,0]
# for r in range(R):
#     for c in range(C):
#         if field[r][c] != '#':
#             s, w = dfs([[r,c]])
#             ans[0] += s
#             ans[1] += w

# print(*ans)


    

