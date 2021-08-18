import sys
N = int(sys.stdin.readline())
sticks = []
for _ in range(N):
    sticks.append(int(sys.stdin.readline()))
cnt = 1
maxs = sticks[-1]
for s in sticks[::-1]:
    if maxs < s:
        maxs = s
        cnt += 1
print(cnt)
