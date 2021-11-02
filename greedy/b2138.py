# 최소 횟수로 같아 지려면 차례대로 목적 전구와 맞아야 되므로
# 현재에서 앞쪽에 있는 전구를 바꿔야 한다면 현재를 누르고, 
# 아닌 경우는 바꾸지 않고 다음 인덱스로 넘어감
# 첫번째는 앞쪽이 없으므로 첫번째 전구를 누르는 경우와 아닌 경우 두가지로 나눠서 확인

d = [-1, 0, 1]
def flip(i):
    for k in range(3):
        ni = i+d[k]
        if ni in range(N):
            bulb[ni] ^= 1

def check(cnt):
    for i in range(1, N):
        if bulb[i-1] == obj[i-1]: continue
        else:
            cnt += 1
            flip(i)
    return cnt if bulb == obj else -1

N = int(input())
arr = list(map(int, input()))
obj  = list(map(int, input()))

bulb = arr[:]
flip(0)
cnt1 = check(1)

bulb = arr[:]
cnt2 = check(0)

if cnt1 != -1 and cnt2 != -1:
    ans = min(cnt1, cnt2)
elif cnt1 == -1 and cnt2 ==-1:
    ans = -1
else:
    ans = max(cnt1, cnt2)
print(ans)

