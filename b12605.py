'''
띄어쓰기로 되어있는 부분을 split으로 구분하여 list로 만들고
list를 뒤집어서 join 함수로 출력
'''
for tc in range(1, int(input())+1):
    words = input().split(' ')
    print('Case #{}: {}'.format(tc, ' '.join(map(str, words[::-1]))))