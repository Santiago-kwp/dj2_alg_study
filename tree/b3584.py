'''
자식노드를 인덱스로 부모노드를 해당 인덱스의 값으로 저장하는
리스트를 정의하여,
A, B 각 자식의 부모노드를 저장하는 리스트를 만들어
하나씩 꺼내서 확인하는 Brute-Force
'''
for _ in range(int(input())):
    N = int(input())
    parents = [0]*10001
    for _ in range(N-1):
        p, c = map(int, input().split())
        parents[c] = p
    A, B = map(int, input().split())
    Ap, Bp = [A], [B]
    while parents[A]: 
        A = parents[A]  
        Ap.append(A)
    while parents[B]: 
        B = parents[B]  
        Bp.append(B)
    for i in Ap:
        if i in Bp:
            print(i)
            break
    

