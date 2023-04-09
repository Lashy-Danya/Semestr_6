class LFSR:
    def __init__(self, seed, poly = 0b10100):
        self.state = seed
        self.poly = poly # порождающий полином: x^5 + x^3 + 1

    def rand(self):
        output = self.state & 1
        self.state >>= 1
        if output:
            self.state ^= self.poly
        return output
    
    def generate_sequence(self, size):
        return [self.rand() for _ in range(size)]

if __name__ == '__main__':
    from collections import Counter

    lfsr = LFSR(0b11011)
    
    arr = []

    for i in range(1000):
        rand_int = 0
        for j in range(5):
            rand_int |= lfsr.rand() << j
        arr.append(rand_int)

    # print(arr)

    count_number = Counter(arr)
    print(len(count_number))
