'''
문제 그대로 리스트에서 제거하고 재귀호출 후 다시 더하는 로직으로 구현, 
j번째가 빠질 때, 
j-1번과 j번(j+1번이 앞으로)을 곱한 값을 더함
'''
N = int(input())
b = list(map(int, input().split()))
maxe = 0
def dfs(i,s):
    global maxe
    if len(b)==2:
        if maxe < s:
            maxe = s
        return
    else:
        for j in range(1,len(b)-1):
            t = b.pop(j)
            dfs(j,s+b[j-1]*b[j])
            b.insert(j,t)
dfs(0,0)
print(maxe)

