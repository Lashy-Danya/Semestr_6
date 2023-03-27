class BBS:
    def __init__(self, seed, p=2147483647, q=2147483647):

        if p % 4 != 3 or q % 4 != 3:
            raise ValueError('p и q должны быть простыми числами')

        self.p = p
        self.q = q
        self.n = p * q
        self.x = seed
    
    def rand(self):
        self.x = (self.x ** 2) % self.n
        return self.x & 0xFFFF  # выбираем 16 младших битов
    
    def generate_sequence(self, size):
        return [self.rand() for _ in range(size)]
    
    def generate_random_array(self, size, minimum, maximum):
        return [minimum + (self.rand() % (maximum - minimum + 1)) for _ in range(size)]

if __name__ == '__main__':
    
    bbs = BBS(12345)
    arr = bbs.generate_random_array(1000, -10, 20)
    print(arr)