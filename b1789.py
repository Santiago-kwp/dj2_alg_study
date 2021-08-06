S = int(input())
n = 1
tot = 0
while(S>tot):
    tot = (1+n)*n/2
    if S-tot <= n:
        break
    n += 1

print(n)

print(int(((int(input())*8+1)**.5-1)/2))