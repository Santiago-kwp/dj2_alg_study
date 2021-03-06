'''
1~N 번까지 N 명의 사람이 원으로 앉아있음
1 2 3 4 5 6 7 중 K번째 사람을 제거 Ex. K=3, idx = 2 = (0+2)%7
1 2 4 5 6 7 : 4부터 첫번째이므로 6 제거, idx = 4 = (2+2)%6
1 2 4 5 7   : 7부터 첫번째이므로 2 제거, idx = 1 = (4+2)%5
1 4 5 7     : 4부터 첫번째이므로 7 제거, idx = 3 = (1+2)%4
1 4 5       : 1부터 첫번째이므로 5 제거, idx = 2 = (3+2)%3

'''
# N, K = map(int, input().split())

# Nlist = list(range(1,N+1))
# stack = []
# i = 0
# while N:
#     i = (i + K-1)%N
#     stack.append(Nlist[i])
#     del Nlist[i]
#     N -= 1
    
# print('<{}>'.format(', '.join(map(str, stack))))

'''
숏코딩
:= walrus operator
역할 : 표현식(Expression)에 이름을 부여하고 재사용할 수 있게 하는 것이다.
'''

n,k=map(int,input().split())
c,*a=range(n+1)     #
print(c)
print(*a)
print(type(a))
a.pop(3)
print(*a)
# print(f'<{str([a.pop(c:=(c+k-1)%b)for b in a[::-1]])[1:-1]}>')