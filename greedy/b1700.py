N, K = map(int, input().split())
order = list(map(int, input().split()))
plug = set()
i = cnt = 0 
while len(plug) < N and i<K:
    plug.add(order[i])
    i += 1

# 플러그가 꽉 찬 경우
# 현재의 꽂혀 있는 애들 중 다음에 쓸게 없으면 바로 return
# 현재 꽂혀 있는 애들이 다 이후에 나온다면 가장 나중에 나온애를 찾아서 리턴
def pick_remove():
    latest = 0
    for p in plug:
        if not p in order[i:]:
            return p
        else:
            idx = order[i:].index(p)
            if idx > latest:
                latest = idx
    return order[i:][latest]

while i< K:
    if not order[i] in plug:
        plug.remove(pick_remove())
        plug.add(order[i])
        cnt += 1
    i += 1
print(cnt)