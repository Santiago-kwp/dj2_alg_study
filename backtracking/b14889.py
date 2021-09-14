N = int(input())
status = [list(map(int, input().split())) for _ in range(N)]
team = [0]*N # 0 은 start team, 1은 link 팀
mins = 1E6

def calc_status(team):
    start, link = [], []
    for i in range(N):
        if team[i]:
            link.append(i)
        else:
            start.append(i)
    start_sum = link_sum = 0
    for i,r in zip(start,link):
        for j,c in zip(start,link):
            start_sum += status[i][j]
            link_sum += status[r][c]

    return abs(start_sum-link_sum)


def div_team(i, n): # i 는 team의 인덱스, n은 link팀의 팀원 수
    if i >= N:      # 인덱스 에러 방지!
        return
    global mins
    if n == N//2:
        st = calc_status(team)
        if st < mins:
            mins = st
        return
    else:
        team[i] = 1       # 한명이 link팀이 된다면 
        div_team(i+1,n+1) # 다음 팀원을 확인하고, link팀의 개수를 +1
        team[i] = 0       # 한명이 start팀이라면,
        div_team(i+1,n)   # 다음 팀원을 확인하러 가고, link팀의 개수는 그대로
div_team(0,0)
print(mins)

    
