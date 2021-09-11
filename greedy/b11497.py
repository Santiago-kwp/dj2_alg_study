'''
풀이 과정 : 제일 큰 수를 중앙에 놓고
그 다음 큰 수 2개를 양 옆에 
그 다음 큰 수 2개 그 양 옆에(순서 유지하며 : 5, 7 -> 2, 4) 
Ex. 2 4 5 7 9 =>  2 <  5 < 9 > 7 > 4
'''
for _ in range(int(input())):
    N = int(input())
    logs = list(map(int, input().split()))
    logs.sort()
    nlogs = [0]*N
    for i in range(N//2):
        nlogs[i], nlogs[N-i-1] = logs[2*i], logs[2*i+1]

    if N%2:
        nlogs[N//2] = logs[-1]

    max_log = nlogs[-1] - nlogs[0]
    for i in range(N-1):
        if max_log < abs(nlogs[i]-nlogs[i+1]):
            max_log = abs(nlogs[i]-nlogs[i+1])
    
    print(max_log)


'''
숏코딩
'''

exec('input();a=sorted(map(int,input().split()));print(max(q-p for p,q in zip(a,a[2:])));'*int(input()))    
    
    