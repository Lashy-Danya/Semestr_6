from sympy.ntheory import factorint
    
class DH:
    def __init__(self, p, private_key):
        self.p = p
        self.g = self.__find_primitive_element(p)
        self.private_key = private_key

    def get_p(self):
        return self.p
    
    def set_p(self, p):
        self.p = p
        self.g = self.__find_primitive_element(p)

    def get_g(self):
        return self.g

    def generate_public_key(self):
        """
        Вычисление открытого ключа
        """
        return (self.g**self.private_key) % self.p
    
    def generate_key(self, public_key):
        """
        Вычисление ключа на основе открытого ключа второго абонента
        """
        return (public_key**self.private_key) % self.p

    def __is_primitive_element(self, g, p):
        """
        Проверка, является ли элемент g примитивным элементом в поле GF(p)
        """
        # проверка g является элемент поля GF(p)
        if pow(g, p-1, p) != 1:
            return False
        
        for i in range(1, p):
            # если i является простым с p, то может быть примитивным элементом
            if pow(g, p-1, p) == 1:
                # проверка, что i не является квадратом другого элемента
                if all(pow(i, (p-1) // q, p) != 1 for q in factorint(p-1)):
                    return True
            
        return False
    
    def __find_primitive_element(self, p):
        """
        Полным перебором находим прмитивный элемент в поле GF(p)
        """
        for g in range(2, p):
            if self.__is_primitive_element(g, p):
                return g
            
        return None

if __name__ == ('__main__'):
    p = 37
    private_key_user1 = 1
    private_key_user2 = 34
    
    '''
    создаем 1 и 2 абонента, передовая публичный ключ p 
    также передаем для каждого свой приватный известный только им
    ''' 
    user1 = DH(p, private_key_user1)
    user2 = DH(p, private_key_user2)

    # вычисляем открытый ключ для каждого
    public_key_user1 = user1.generate_public_key()
    public_key_user2 = user2.generate_public_key()

    # вычисляем ключи на основе полученных публичных ключей
    key_user1 = user1.generate_key(public_key_user2)
    key_user2 = user2.generate_key(public_key_user1)

    print(f'Key User 1: {key_user1}')
    print(f'Key User 2: {key_user2}')