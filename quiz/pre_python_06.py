"""6. 아래와 같이 별이 찍히게 출력하시오.
숫자를 입력하세요 : 5
    ★
   ★★
  ★★★
 ★★★★
★★★★★
 ★★★★
  ★★★
   ★★
    ★

예시
<입력>
숫자를 입력하세요 : 5

<출력>
    ★
   ★★
  ★★★
 ★★★★
★★★★★  
 ★★★★
  ★★★
   ★★
    ★


"""
n = int(input('숫자를 입력하세요 :'))
for i in range(1, n*2):
    if i <= n:
        s = '★'*i
        s = s.rjust(n)
    else:
        s = '★' * (n*2-i)
        s = s.rjust(n)
    print(s)