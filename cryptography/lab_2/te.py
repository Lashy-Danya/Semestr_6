def lfsr(seed, taps):
    """
    seed: начальное состояние регистра сдвига в виде списка из 0 и 1
    taps: список позиций, на которые умножаются биты регистра для получения следующего бита в последовательности
    """
    while True:
        yield seed[0]
        xor = 0
        for tap in taps:
            xor ^= seed[tap]
        seed.pop()
        seed.insert(0, xor)

if __name__ == '__main__':
    from collections import Counter

    lfsr = lfsr([1, 0, 0, 0], [3, 4])
    
    arr = []

    for i in range(1000):
        rand_int = 0
        for j in range(5):
            rand_int |= next(lfsr) << j
        arr.append(rand_int)

    count_number = Counter(arr)
    print(len(count_number))