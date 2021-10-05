'''
왼쪽으로 지나가는 차만 고려하면 되므로 문제에 적혀있는대로
딕셔너리를 통해 +500, +1000, +1500을 값으로 두고 해당 값이 왼쪽 키, 오른쪽 키에 존재하는지 찾는 코드
'''
n = int(input())
for _ in range(n):
    m = int(input())
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))

    left_dict, right_dict = {}, {}
    for l in left:
        left_dict[l] = [l+500, l+1000, l+1500]
    for r in right:
        right_dict[r] = 1
    cnt = 0
    for key, val in left_dict.items():
        if val[0] in left_dict and val[1] in right_dict and val[2] in right_dict:
            cnt += 1

    print(cnt)

