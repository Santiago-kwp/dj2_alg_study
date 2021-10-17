'''
1. 뒤부터 인덱스와 같이 반복문으로 접근하면서 최대값이 갱신되면 해당 인덱스를 total에 더해줌
2. 최대값이 아닐 경우, 스택 여부와 스택의 탑을 확인하여 현재 값보다 같거나 클때까지 pop을 해줌
3. 최대값이 아니기 때문에 스택에 최소 한 개는 남아있고, 스택의 탑의 원소의 인덱스 값과 현재 인덱스의 차이-1 을 total에 더해줌
'''
import sys
N = int(input())
total = maxN = 0
arr, stack = [], []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
    
for i, a in enumerate(arr[::-1]):
    if a > maxN:
        total += i
        maxN = a
    else:
        while a > stack[-1][0]:
            stack.pop()
        total += i-stack[-1][1]-1
    stack.append((a, i))
    
print(total)
    
    
