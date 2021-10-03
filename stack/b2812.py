'''
1. 숫자를 지워도 만들 수 있는 자리수를 남긴 상태에서 맨 앞자리 수가 가장 커야함
2. 스택에 첫째자리수부터 하나씩 넣고 다음 숫자랑 비교하여 다음 숫자가 크면 스택에서 pop
3. 이미 지울 수가 없어서 K=0 이 되거나, 스택에 있는 숫자가 아직 만들어야 되는 수보다 부족한 경우 push
'''
N, K = map(int, input().split())
# R = 남게 되는 숫자의 자리 수
R = N-K
# map iterable 객체로 입력을 받음 Ex. 1924 -> [1, 9, 2, 4]
num = [*map(int,list(input()))]

# 스택에는 가장 큰 수가 되도록 쌓을 예정
# 스택 초기화
stack = []
# for loop를 돌면서 ...
for n in num:
    # while문 반복 조건: 지울 숫자가 남아 있고(K>0), 스택에 숫자가 있고(stack), 
    # 스택의 맨 윗 숫자(stack[-1])보다 다음 숫자(n)가 크면
    # 지울 숫자를 하나 지우고(K-=1) 스택에서 pop
    while K and stack and n > stack[-1]:
        K -= 1
        stack.pop()
        
    # 다 지워서 K가 0 이거나, 
    # 스택에 있는 숫자가 만들어야 될 수보다 부족한 경우 스택에 넣음
    if not K or len(stack) < R:
        stack.append(n)

print(''.join(map(str, stack)))
