S = int(input())
n = 1
tot = 0
while(S>tot):
    tot = (1+n)*n/2
    if S-tot <= n:
        break
    n += 1

print(n)

'''
# print(int(((int(input())*8+1)**.5-1)/2))
숏코딩 정답이라는데 n(n+1)/2 - N > 0 이 되는 경우를 n에 대한 근의 공식으로 풀어서
n의 근으로 시각복잡도를 아주 짧게 가져간 방법.
'''
