class LFSR:
    def __init__(self, seed, polynomial):
        self.state = seed
        self.polynomial = polynomial
    
    def shift(self):
        feedback = 0
        for i in self.polynomial:
            feedback ^= self.state >> i & 1
        self.state = (self.state >> 1) | (feedback << 4)
        return self.state & 1

if __name__ == '__main__':
    seed = 0b101101
    polynomial = [5, 2]

    lfsr = LFSR(seed, polynomial)

    arr = []

    for i in range(10):
        rand_int = 0
        for j in range(8):
            rand_int |= lfsr.shift() << j
        arr.append(rand_int)

    print(arr)
