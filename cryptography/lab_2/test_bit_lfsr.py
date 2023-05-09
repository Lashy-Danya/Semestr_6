class LFSR:
    def __init__(self, seed, poly):
        self.state = seed
        self.poly = poly
        self.deg = len(poly)
    
    def shift(self):
        out = self.state & 1
        bit = 0
        for i in range(self.deg):
            if self.poly[i]:
                bit ^= self.state >> i & 1
        value = (self.state >> 1) | (bit << (self.deg - 1))
        # print(f'state: {bin(self.state)} | bit: {bit} | out: {out}')
        self.state = value
        return out
    
    def rand(self):
        return sum(self.shift() << i for i in range(self.deg))
        # rand_int = 0
        # for i in range(self.deg):
        #     rand_int |= self.shift() << i
        # return rand_int

if __name__ == '__main__':
    lfsr = LFSR(0b11011, [1,0,1,0,0])

    mas_arr = [lfsr.rand() for _ in range(32)]
    
    print(mas_arr)