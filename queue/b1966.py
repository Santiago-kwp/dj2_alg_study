from collections import deque
for _ in range(int(input())):
    N, M = map(int, input().split())
    pages = []
    n = 1
    for w in map(int, input().split()):
        pages += [(n, w)]
        n += 1
    obj = pages[M]
    pages = deque(pages)
    q = 0
    while pages:
        maxi = -1
        maxw = 0
        # 가장 큰 우선 순위를 가진 인덱스 반환
        for i in range(len(pages)):
            if pages[i][1] > maxw:
                maxw = pages[i][1]
                maxi = i
        q += 1
        for _ in range(maxi):
            pages.append(pages.popleft())

        if obj == pages.popleft():
            print(q)
            break
