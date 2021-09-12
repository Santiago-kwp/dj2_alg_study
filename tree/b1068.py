'''
딕셔너리 구조를 활용하여 부모 노드를 키, 자식노드를 값으로 정의 후
삭제 로직과 단말노드 계산 로직을 재귀 함수로 각각 구현
'''
N = int(input())
tree = {}
for i, p in enumerate(input().split(' ')):
    p = int(p)
    try: tree[p].append(i)
    except: tree[p] = [i]
r = int(input())

for ch in tree.values():
    if r in ch:
        ch.remove(r)

def delt(r):
    if r in tree.keys():
        for a in tree[r]:
            delt(a)
        del tree[r]

cnt = 0 
def calc(i):
    global cnt
    try:
        if i != -1 and not tree[i]:
            cnt+= 1
        for t in tree[i]:
            calc(t)
    except:
        cnt += 1

delt(r)
calc(-1)
print(cnt)