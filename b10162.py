T = int(input())
nums = ''
if T%10:
    print('-1')
else:
    for t in [300, 60, 10]:
        nums+= f' {T//t}'
        T -= (T//t)*t 
    print(nums[1:])
