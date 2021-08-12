for tc in range(int(input())):
    N, M = input().split()
    # 자리수가 다른데 쌍이면 교환 가능
    # 1의 수가 다르면 추가 가능
    cnt = 0
    N_diff = 0
    M_diff = 0
    tot_diff = 0
    for i in range(len(N)):
        if N[i] != M[i]:
            tot_diff += 1
            # if N[i]:
            #     N_diff += 1
            # else:
            #     M_diff += 1
    num_diff = abs(N.count('1') - M.count('1'))
    ans = (tot_diff - num_diff) //2 + num_diff
    print(ans)
        


            


