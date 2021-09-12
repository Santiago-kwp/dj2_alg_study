'''
재귀호출하여 전위, 중위, 후위 순회 구현
'''
def pre(i):
    if i !='.':
        print(i,end="")
        pre(alpha[i][0])
        pre(alpha[i][1])

def ino(i):
    if i !='.':
        ino(alpha[i][0])
        print(i,end="")
        ino(alpha[i][1])

def post(i):
    if i !='.':
        post(alpha[i][0])
        post(alpha[i][1])
        print(i,end="")
        
N = int(input())
alpha = {}
for i in range(1,N+1):
    r, lc, rc = input().split(' ')
    alpha[r] = [lc, rc]

for f in ['pre', 'ino', 'post']:
    eval(f)('A')
    print()