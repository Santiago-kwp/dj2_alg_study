'''
5번 프렛 누를 때 7번은 그냥 누르면 7번 소리나고
5, 7번 누른 상태일 때 2번 프렛은 5, 7번 떼고 2번 눌러야 소리남
같은 음일 때 스택에 쌓여있는 프렛보다 높으면 그냥 쌓고, 같으면 아무것도 안함
스택의 맨 위 프렛이 낮을 때까지 pop하고, 
'''
import sys
N, P = map(int, input().split())
guitar = [ [] for _ in range(7)]
cnt = 0
for _ in range(N):
    l, p = map(int, sys.stdin.readline().split())
    while guitar[l] and guitar[l][-1] > p:
        guitar[l].pop()
        cnt += 1
    if not guitar[l]:
        guitar[l].append(p)
        cnt += 1
    else:
        if guitar[l][-1] < p:
            guitar[l].append(p)
            cnt += 1
print(cnt)
        

