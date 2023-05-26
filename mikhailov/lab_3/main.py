from abc import ABC

class FloweringPlant(ABC):
    def __init__(self, name, color, number_of_petals):
        self.__name = name
        self.color = color
        self.number_of_petals = number_of_petals

    @property
    def name(self):
        return self.__name
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def number_of_petals(self):
        return self.__number_of_petals
    
    @property
    def living_life(self):
        return self.__living_life
    
    @number_of_petals.setter
    def number_of_petals(self, number_of_petals):
        if int(number_of_petals) < 0:
            raise ValueError(f"Количество лепестков должно быть больше 0")
        self.__number_of_petals = number_of_petals

    def deserialize(FloweringPlant_str):
        str_parts = FloweringPlant_str.split(',')
        if str_parts[0] == 'Однолетние':
            return AnnualFloweringPlant(str_parts[1], str_parts[2], int(str_parts[3]), int(str_parts[4]))
        elif str_parts[0] == 'Многолетние':
            return PerennialFlowerPlant(str_parts[1], str_parts[2], int(str_parts[3]), int(str_parts[4]))
        

class AnnualFloweringPlant(FloweringPlant):
    def __init__(self, name, color, number_of_petals, living_life):
        super().__init__(name, color, number_of_petals)
        self.living_life = living_life

    def __str__(self):
        return f"Однолетние,{self.name},{self.color},{self.number_of_petals},{self.living_life}"

    @property
    def living_life(self):
        return self.__living_life
    
    @living_life.setter
    def living_life(self, living_life):
        if int(living_life) > 1:
            raise ValueError("Однолетние растение не может жить больше года")
        self.__living_life = living_life

class PerennialFlowerPlant(FloweringPlant):
    def __init__(self, name, color, number_of_petals, living_life):
        super().__init__(name, color, number_of_petals)
        self.living_life = living_life

    def __str__(self):
        return f"Многолетние,{self.name},{self.color},{self.number_of_petals},{self.living_life}"
    
    @property
    def living_life(self):
        return self.__living_life
    
    @living_life.setter
    def living_life(self, living_life):
        if int(living_life) <= 1:
            raise ValueError("Многолетнее растение не может быть меньше года")
        self.__living_life = living_life

def parse_db():
    db = []
    with open('data.txt') as data_file:
        for line in data_file.readlines():
            if len(line) > 0:
                db.append(FloweringPlant.deserialize(line.strip("\r\n ")))

    return db

def save_db():
    with open('data.txt', 'w') as data_file:
        data_file.write('\n'.join(map(str, db)))

def find_entry(name):
    for e in db:
        if e.name == name:
            return e
    return None

def add_entry(e):
    if find_entry(e.name) is None:
        db.append(e)
        save_db()
        print(f'Запись добавлена', end='\n\n')
    else:
        raise ValueError(f"Запись с таким же именем уже есть в базе данных")
    
def remove_entry(name):
    e = find_entry(name)
    if e is not None:
        db.remove(e)
        save_db()
        print(f"Запись удалина", end='\n\n')
    else:
        raise ValueError(f"Запись с таким именем не найдена в базе данных")

db = parse_db()

while(True):
    command = None
    while command not in ['найти', 'добавить', 'удалить', 'выйти']:
        command = input("Выберите команду (найти / добавить / удалить / выйти): ")
    if command == 'найти':
        e = find_entry(input('Название: '))
        if e is not None:
            print(f"Цвет: {e.color}\nКоличество лепестков: {e.number_of_petals}\nСрок жизни в годах: {e.living_life}", end='\n\n')
        else:
            print(f"Запись с таким именем не найдена в базе данных", end='\n\n')
    elif command == 'добавить':
        vclass = None
        while vclass not in ['Однолетние', 'Многолетние']:
            vclass = input("Тип цветкового растения (Однолетние, Многолетние): ")
            name = input('Название: ')
            color = input('Цвет: ')
            number_of_petals = input('Количество лепестков: ')
            living_life = input('Время жизни в годах: ')
            if vclass == 'Однолетние':
                try:
                    add_entry(AnnualFloweringPlant(name, color, number_of_petals,
                                        living_life))
                except ValueError as e:
                    print(e)
            else:
                try:
                    add_entry(PerennialFlowerPlant(name, color, number_of_petals,
                                        living_life))
                except ValueError as e:
                    print(e)
    elif command == 'удалить':
        try:
            remove_entry(input('Название: '))
        except ValueError as e:
            print(e)
    else:
        exit()