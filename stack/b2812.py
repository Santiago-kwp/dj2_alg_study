'''
생각보다 안되는 케이스가 많아서 헤맨 문제
N자리 숫자를 숫자 하나씩 리스트로 받고, 
K가 남아 있고, 스택에 숫자가 있고, 스택의 맨 위 숫자보다 클 경우에만
숫자 하나를 제외하고 pop
그 외의 경우 중 K가 이미 0이거나, 남은 스택길이가 이미 다 찬 경우에 push
'''
N, K = map(int, input().split())
R = N-K
num = [*map(int,list(input()))]

stack = [num[0]]
for n in num[1:]:
    while K and stack and n>stack[-1]:
        K -= 1
        stack.pop()
    if not K or len(stack) < R:
        stack.append(n)

print(''.join(map(str, stack)))
