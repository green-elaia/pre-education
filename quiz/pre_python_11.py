"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""
def gcd(a, b):
    if a >= b:
        g = b
    else:
        g = a

    for i in range(g, 0, -1):
        if a % i == 0 and b % i == 0:
            g = i
            break
    else:
        g = 1
    return g

print(gcd(12, 6))
