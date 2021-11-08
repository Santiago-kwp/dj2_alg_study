# 오큰수
N = int(input())
arr = list(map(int, input().split()))
# 전략: 뒤부터 앞으로 보면서
# 현재 스택의 탑에 있는 수보다 작으면 
# 스택의 탑에 있는 수를 정답에 넣고, 스택에 쌓음
# 현재 스택의 탑에 있는 수보다 같거나 크면
# 스택의 탑의 수가 더 클 때까지 pop, 비었으면 -1 하고 스택에 쌓음
# 그 수가 있으면 해당 수를 정답에 넣고, 스택에 쌓음
ans = [0]*N
stack = []

for i in range(N-1,-1,-1):
    flag = 1
    while stack:
        if arr[i] < stack[-1]:
            ans[i] = stack[-1]
            stack.append(arr[i])
            flag = 0
            break
        else:
            stack.pop()
    if flag:
        ans[i] = -1
        stack.append(arr[i])
            
print(*ans)
