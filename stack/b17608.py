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

'''
숏코딩
'''
import sys
input()
a=[int(i)for i in sys.stdin][::-1]
top=a[0]
c=1
for i in a[1:]:
    if i>top:c+=1;top=i
print(c)