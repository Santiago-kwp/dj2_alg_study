n = int(input())
i=n//5
while(i>=0):
    if (n-5*i)%3:
        i-=1
    else:
        x,y = i, (n-5*i)//3
        break

print('-1' if i < 0 else x+y)


