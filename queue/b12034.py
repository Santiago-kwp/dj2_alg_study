'''
뒤에꺼 하나 빼서 
앞에부터 하나씩 비교하면서 같으면 정답에 append 하고 원래 리스트에서 삭제
마지막에 거꾸로 해서 출력
'''

for tc in range(1, int(input())+1):
    N = int(input())
    prices = list(map(int,input().split()))
    ans = []
    while(len(ans)<N):
        big = prices.pop()
        for i in range(len(prices)):
            if prices[i] == 0.75*big:
                ans.append(prices[i])
                prices.pop(i)
                break
    print('Case #{}: {}'.format(tc, ' '.join(map(str,ans[::-1]))))

