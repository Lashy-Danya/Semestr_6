from math import gcd

# функция эйлера
def euler(x):
    r = 0
    for i in range(1, x):
        if gcd(x, i) == 1:
            r += 1
    return r

# получение простых чисел p и q зная n
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def find_p_and_q(n, p):
    q = n // p
    while (p * q) != n:
        p += 1
        q = n // p

    return p, q

n = 473 #

p, q = find_p_and_q(n, 2)
print(f'p = {p} | q = {q}')

fn = euler(n)
print(f'fn: {fn}')

# выбираем число e (открытая экспонента)
# это простое число и в идеале число Ферма
# e должна быть взаимо простым числом с n ???
e = 17 #

# получаем число используя функцию эйлера
d = e ** (euler(euler(n)) - 1) % fn
print(f'd: {d}')

# зашифровка сообщения
c = 471 #

# расшифровка сообщения
m = c ** d % n
print(f'm: {m}')

# print(m ** e % n)