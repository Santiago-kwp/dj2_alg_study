snew = ''
ans = 'UCPC'
j=0
for s in input():
    if s == ans[j]:
        snew+=s
        j+=1
        if j>3:
            break
        
if snew == 'UCPC':
    print("I love UCPC")
else:
    print("I hate UCPC")