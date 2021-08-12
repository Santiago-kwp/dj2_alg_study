'''
1의 개수가 차이나면 매꿔야 되고 
개수 차이를 제외한 자리수가 다른 경우를 2로 나누면 교환 성립 
'''
for tc in range(int(input())):
    N, M = input().split()
    tot_diff = 0
    for i in range(len(N)):
        if N[i] != M[i]:
            tot_diff += 1
    num_diff = abs(N.count('1') - M.count('1'))
    ans = (tot_diff - num_diff) //2 + num_diff
    print(ans)        


            


