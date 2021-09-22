'''
이진트리 원소와 왼/오른쪽 이동 개수의 규칙성을 찾아 코드로 구현
'''
A, B = map(int, input().split())
l=r=0
while ([A,B] != [1,1]):
    if A == 1:
        r += B-A
        B = 1
    elif B == 1:
        l += A-B
        A = 1
    if A > B:
        l += A//B
        A %= B
    if A < B:
        r += B//A
        B %= A
print(l, r)