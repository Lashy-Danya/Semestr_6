from math import gcd

# функция эйлера
def euler(x):
    r = 0
    for i in range(1, x):
        if gcd(x, i) == 1:
            r += 1
    return r

p = 11
q = 29
n = p * q
fn = (p - 1) * (q - 1)
print(f'euler: {euler(n)}')
print(f'(p-1)*(q-1): {fn}')

# выбираем число e (открытая экспонента)
# это простое число и в идеале число Ферма
# e должна быть взаимо простым числом с n ???
e = 3

# получаем число используя функцию эйлера
d = e ** (euler(euler(n)) - 1) % fn
print(d)

# зашифровка сообщения
m = 10
c = m ** e % n

# расшифровка сообщения
print(c ** d % n)