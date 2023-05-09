# Режимы шифрования/дешифрования
ECB = 0
CBC = 1
CFB = 2
OFB = 3
CFB_WIKI = 4
OFB_WIKI = 5

ENCRYPT = 0
DECRYPT = 1

class DES:

    # Начальная перестановка IP
    __IP = [
        58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24,16, 8,
        57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7
    ]

    # Таблица расширения для преобразования 32-битных блоков в 48-битные
    __EXPANSION_TABLE = [
        32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1
    ]

    # Таблицы S-box для преобразования из 48-бит в 32-бита
    __S_BOX = [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
        0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
        4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
        15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
        3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
        0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
        13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
        13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
        13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
        1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
        13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
        10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
        3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
        14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
        4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
        11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
        10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
        9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
        4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
        13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
        1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
        6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
        1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
        7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
        2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11], 
    ]

    # Таблица перестановки P, испольхуемая на выходе S-блоков
    __P = [
        16, 7, 20, 21, 29, 12, 28, 17,
        1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9,
        19, 13, 30, 6, 22, 11, 4, 25
    ]

    # Конечная перестановка IP^-1
    __FP = [
        40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25
    ]

    # Число сдвига влево
    __LEFT_ROTATIONS = [
        1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
    ]

    # Таблицы перестановки и перевода
    __K1P = [
        57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36
    ]

    __K2P = [
        63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
    ]

    # Таблицы CP для преобразования из 56-бит в 48-бит
    __CP = [
        14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
    ]

    def __init__(self, key, mode=ECB, iv=None):
        if len(key) != 8:
            raise ValueError('Недопустимый размер ключа DES. Ключ должен иметь длину ровно 8 байт.')
        
        self.block_size = 8
        self.key_size = 8
        self._mode = mode
        self._iv = iv
        self.key = key

        self.L = []
        self.R = []
        self.keys = []
        self.result = []

        self.setKey(key)

    def getMode(self):
        return self._mode
    
    def setMode(self, mode):
        self._mode = mode

    def getKey(self):
        return self.key
    
    def setKey(self, key):
        self.key = key
        self.__create_keys()

    def getIV(self):
        return self._iv
    
    def setIV(self, iv):
        if not iv or len(iv) != self.block_size:
            raise ValueError(f'Недопустимое начальное значение, должно быть кратно {self.block_size} байт')
        self._iv = iv

    def __string_to_bitList(self, data):
        """
        Возвращает массив битов (0, 1) каждого символа.
        Где символ закодирован в кодировке cp866
        """
        return [int(bit) for ch in bytes(data, 'cp866') \
                for bit in bin(ch)[2:].zfill(8)]
    
    def __bitList_to_string(self, data):
        """Возвращает строку. Кодирая в кодировке cp866"""
        bytes_hex = bytes([int(''.join(str(bit) for bit in data[i:i+8]), 2) \
                           for i in range(0, len(data), 8)])
        return bytes_hex.decode('cp866')

    def __permutation(self, block, table):
        """Перестановка в блоке с указанием таблицы"""
        return list(map(lambda x: block[x - 1], table))

    def __create_keys(self):
        """Создание 16 ключей для каждого раунда"""
        self.L = self.__permutation(self.__string_to_bitList(self.getKey()), DES.__K1P)
        self.R = self.__permutation(self.__string_to_bitList(self.getKey()), DES.__K2P)

        for i in range(16):
            j = 0
            while j < DES.__LEFT_ROTATIONS[i]:
                self.L.append(self.L[0])
                del self.L[0]

                self.R.append(self.R[0])
                del self.R[0]

                j += 1

            self.keys.append(self.__permutation(self.L + self.R, DES.__CP))

    def __des_crypt(self, block, crypt_type):
        """Реализация DES-зашифрования/расшифрования"""
        block = self.__permutation(block, DES.__IP)
        self.L = block[:32]
        self.R = block[32:]

        if crypt_type == ENCRYPT:
            keys = self.keys
        else:
            keys = self.keys[::-1]

        # 16 раундов сети Файстеля
        for i in range(16):
            # создание копии R[i-1] для L[i] 
            temp = self.R

            # расширение R[i-1] с 32 бит до 48 бит
            self.R = self.__permutation(self.R, DES.__EXPANSION_TABLE)
            # XOR между R и Kn
            self.R = list(map(lambda x, y: x ^ y, self.R, keys[i]))
            # создание sub-box-ов по 6 бит каждый
            sub_box = [
                self.R[:6], self.R[6:12], self.R[12:18], self.R[18:24],
                self.R[24:30], self.R[30:36], self.R[36:42], self.R[42:]
            ]

            # соединяем все sub-box в один 32 бит
            box = [0] * 32
            pos = 0

            for j in range(8):
                m = (sub_box[j][0] << 1) + sub_box[j][5]
                n = (sub_box[j][1] << 3) + (sub_box[j][2] << 2) + (sub_box[j][3] << 1) + sub_box[j][4]

                # значение перестановки
                v = DES.__S_BOX[j][(m << 4) + n]

                box[pos] = (v & 8) >> 3
                box[pos + 1] = (v & 4) >> 2
                box[pos + 2] = (v & 2) >> 1
                box[pos + 3] = v & 1

                pos += 4

            self.R = self.__permutation(self.R, DES.__P)
            # Xor ежду R и L[i-1]
            self.R = list(map(lambda x, y: x ^ y, self.R, self.L))

            self.L = temp

        self.L, self.R = self.R, self.L

        self.result = self.__permutation(self.L + self.R, DES.__FP)

        return self.result
    
    def crypt(self, data, crypt_type):

        if not data:
            return ''
        
        if (self.getMode() != CFB) and (self.getMode() != OFB):
            if len(data) % self.block_size != 0:
                pad = -len(data) % self.block_size
                data += (b'\x00' * pad).decode('cp866')

        if self.getMode() == CBC:
            if self.getIV():
                iv = self.__string_to_bitList(self.getIV())
            else:
                raise ValueError('Для режима CBC необходимо указать начальное значение вектора для шифрования.')
        elif self.getMode() == CFB or self.getMode() == CFB_WIKI:
            if self.getIV():
                iv = self.__string_to_bitList(self.getIV())
            else:
                raise ValueError('Для режима CFB необходимо указать начальное значение вектора для шифрования.')
        elif self.getMode() == OFB or self.getMode() == OFB_WIKI:
            if self.getIV():
                iv = self.__string_to_bitList(self.getIV())
            else:
                raise ValueError('Для режима OFB необходимо указать начальное значение вектора для шифрования')

        result = []

        for i in range(0, len(data), self.block_size):
            block = self.__string_to_bitList(data[i:i+self.block_size])

            if self.getMode() == ECB:
                processed_block = self.__des_crypt(block, crypt_type)
            elif self.getMode() == CBC:
                if crypt_type == ENCRYPT:
                    block = list(map(lambda x, y: x ^ y, block, iv))

                processed_block = self.__des_crypt(block, crypt_type)

                if crypt_type == DECRYPT:
                    processed_block = list(map(lambda x, y: x ^ y, processed_block, iv))
                    iv = block
                else:
                    iv = processed_block
            elif self.getMode() == CFB_WIKI:
                # простая реализация с вики
                processed_block = self.__des_crypt(iv, ENCRYPT)
                processed_block = list(map(lambda x, y: x ^ y, processed_block, block))

                if crypt_type == ENCRYPT:
                    iv = processed_block
                else:
                    iv = block
            elif self.getMode() == OFB_WIKI:
                # простая реализация с вики
                processed_block = self.__des_crypt(iv, ENCRYPT)
                iv = processed_block
                processed_block = list(map(lambda x, y: x ^ y, processed_block, block))
            elif self.getMode() == CFB:
                # число битов блока подблока
                k = 8
                processed_block = []

                for i in range(0, len(block), k):
                    encrypt_iv = self.__des_crypt(iv, ENCRYPT)
                    result_xor = list(map(lambda x, y: x ^ y, encrypt_iv[0:k], block[i:i+k]))
                    processed_block += result_xor
                    del iv[0:k]
                    if crypt_type == ENCRYPT:
                        iv += result_xor
                    else:
                        iv += block[i:i+k]
            elif self.getMode() == OFB:
                # число битов блока подблока
                k = 8
                processed_block = []

                for i in range(0, len(block), k):
                    encrypt_iv = self.__des_crypt(iv, ENCRYPT)
                    result_xor = list(map(lambda x, y: x ^ y, encrypt_iv[0:k], block[i:i+k]))
                    processed_block += result_xor
                    del iv[0:k]
                    iv += encrypt_iv[0:k]

            result.append(self.__bitList_to_string(processed_block))

        return ''.join(result)
    

if __name__ == ('__main__'):

    test = 'Шлепа, скажи кар!!! Kar. Че за nax?'
    # test = '@Шлепа'
    # Ключ и начальный вектор должны быть равны 8 байт
    key = 'ключ64б!'
    iv = 'тестив01'

    # Режим ECB
    # des = DES(key, ECB)
    # shifr = des.crypt(test, ENCRYPT)
    # deshifr = des.crypt(shifr, DECRYPT)

    # Режим CBC
    # des = DES(key, CBC, iv)
    # shifr = des.crypt(test, ENCRYPT)
    # deshifr = des.crypt(shifr, DECRYPT)

    # Режим CFB_WIKI
    # des = DES(key, CFB_WIKI, iv)
    # shifr = des.crypt(test, ENCRYPT)
    # deshifr = des.crypt(shifr, DECRYPT)

    # Режим OFB_WIKI
    # des = DES(key, OFB_WIKI, iv)
    # shifr = des.crypt(test, ENCRYPT)
    # deshifr = des.crypt(shifr, DECRYPT)

    # Режим CFB, где k = 8 bit
    # des = DES(key, CFB, iv)
    # shifr = des.crypt(test, ENCRYPT)
    # deshifr = des.crypt(shifr, DECRYPT)

    # Режим OFB, где k = 8 bit
    des = DES(key, OFB, iv)
    shifr = des.crypt(test, ENCRYPT)
    deshifr = des.crypt(shifr, DECRYPT)

    print(f'Начальный текст: {test}')
    print(f'Зашифрованый текст: {shifr}')
    print(f'Расшифрованый текст: {deshifr}')