'''
문제 주어진 대로 스택으로 1씩 증가시키는 수를 통해 구현
1. 스택이 비었으면 현재 숫자 넣고, 숫자 +1, 
2. 스택에 있을 때 맨 위와 같을 때까지 현재 숫자 넣고 숫자 +1
3. 맨 위랑 같으면 pop하고 다음 볼 숫자로 이동
'''
import sys

def series():
    ans = []
    i, j = 1, 0
    while j < n:
        if stack:
            if stack[-1] > arr[j]:
                return 0
            while stack[-1] != arr[j]:
                stack.append(i)
                ans.append('+')
                i += 1
            stack.pop()
            ans.append('-')
            j += 1
        else:
            stack.append(i)
            ans.append('+')
            i += 1
    return ans

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

stack = []
ans = series()
if ans:
    for s in ans:
        print(s)
else:
    print('NO')
