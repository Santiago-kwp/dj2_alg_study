'''
동전값이 내림차순으로 주어지므로 거꾸로 인덱싱을 하여 
나눠지는 경우 몫만큼 count 하고 나머지를 K 값에 갱신
'''
N, K = map(int,input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
cnt = 0

for coin in coins[::-1]:
    if K//coin:
        cnt += K//coin
        K %= coin

print(cnt)
