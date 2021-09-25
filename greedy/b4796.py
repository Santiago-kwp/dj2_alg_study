'''
몫과 나머지를 이용하되 나머지가 L 보다 큰 경우를 고려하여야 된다!
'''
import sys
I = lambda:map(int, sys.stdin.readline().split())
L, P, V = I()
tc = 1
while L:
    m, d = divmod(V,P)
    print('Case {}: {}'.format(tc, m*L+min(d,L)))
    tc += 1
    L, P, V = I()
