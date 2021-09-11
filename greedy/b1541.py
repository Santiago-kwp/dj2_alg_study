'''
eqn: '40+30-50+40' => '40+30-(50+40)
수식에 '-'를 찾고 '-'이후에 나오는 '+'를 '-'로 바꿔서 
새로운 수식으로 변환 후 풀이하는 방법
split('+')로 나눠진 부분은 더하고 
'-'문자가 있어 나눠지지 않은 수식은
split('-')로 나눠 맨 앞 원소만 더하고 나머지를 뺌
'''
eqn = input()
indm = eqn.find('-')
eqn_new = eqn[:indm] + eqn[indm:].replace('+','-')
ans = 0
for valp in eqn_new.split('+'):
    if '-' in valp:
        ans += int(valp.split('-')[0])
        ans -= sum(map(int,valp.split('-')[1:]))
    else:
        ans += int(valp)

print(ans)
'''
숏코딩
split('-')를 통해 -를 기준으로 수식을 나누고
Ex. '55+40-50+90-40+20' => '55+40', '50+90', '40+20'
각 나눠진 수식 혹은 값을 split('+')로 나눠 값으로 만든 뒤 sum()
을 통해 더한 값을 a와 여러인자를 뜻하는 *b에 저장
만약 위 예시처럼 -로 인해 수식이 나눠졌다면 
맨 앞 95 - (140) -(60) 이므로 a-sum(b)가 성립이 되고
수식에 -가 없어 나눠지지 않았다면 
어차피 인자가 a 하나밖에 안나오므로 성립할 수 있다.
'''
a,*b=[sum(map(int,s.split('+')))for s in input().split('-')]
print(a-sum(b))

for s in input().split('-'):
    a, *b = [sum(map(int,s.split('+')))]
print(a, *b)
