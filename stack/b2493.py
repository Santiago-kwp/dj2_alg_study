'''
인덱스를 들고 다니는 스택을 활용해서 
스택이 있을 때 스택의 탑과 길이 비교하여 현재 h가 스택의 탑보다 크면 작을 때 혹은 스택이 빌 때까지 pop
스택이 남아있는 경우 스택의 탑의 인덱스가 멈추는 곳이므로 ans에 인덱스를 append
스택이 비어있는 경우는 ans에 0을 append
'''
N = int(input())
stack, ans = [], []
for idx, h in enumerate(map(int, input().split()), start = 1):
    while stack and stack[-1][0] < h:
        stack.pop()
    if stack:
        ans.append(stack[-1][1])
        stack.append((h, idx))
    if not stack:
        stack.append((h,idx))
        ans.append(0)

print(*ans)
        