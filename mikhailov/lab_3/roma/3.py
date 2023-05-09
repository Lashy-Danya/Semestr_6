# IF_NEEDED – в момент обращения к слоту,
# IF_ADDED – при подстановке в слот значения, IF_REMOVED – при стирании значения слота.
class FrameFish:

    def __init__(self, family, name, fish_size):
        self.family = family
        self.name = name
        self.if_added_fish_size(fish_size)
        self.fish_size = int(fish_size)

    def get_family(self):
        return self.family

    def get_name(self):
        return self.name

    def get_fish_size(self):
        return self.fish_size

    def if_added_fish_size(self, fish_size):
        if int(fish_size) < 3:
            raise ValueError('Настолько микроскопических рыбок не бывает. Переделай.')
        elif int(fish_size) > 50:
            raise ValueError('Такая грамадина в аквариум не влезит. Переделай.')


class FrameFishViviparous(FrameFish):

    def __init__(self, family, name, fish_size, min_number_of_liters, min_water_temperature, max_water_temperature,
                min_hydrogen_index, max_hydrogen_index, min_water_hardness, max_water_hardness):
        FrameFish.__init__(self, family, name, fish_size)

        self.if_added_min_number_of_liters(min_number_of_liters)
        self.min_number_of_liters = int(min_number_of_liters)

        self.if_added_water_temperature(min_water_temperature, max_water_temperature)
        self.min_water_temperature = int(min_water_temperature)
        self.max_water_temperature = int(max_water_temperature)

        self.if_added_hydrogen_index(min_hydrogen_index, max_hydrogen_index)
        self.min_hydrogen_index = float(min_hydrogen_index)
        self.max_hydrogen_index = float(max_hydrogen_index)

        self.if_added_water_hardness(min_water_hardness, max_water_hardness)
        self.min_water_hardness = int(min_water_hardness)
        self.max_water_hardness = int(max_water_hardness)

    def get_min_number_of_liters(self):
        return str(self.min_number_of_liters)

    def if_added_min_number_of_liters(self, min_number_of_liters):
        if int(min_number_of_liters) < 5:
            raise ValueError('Рыбка от сушника помрёт. Переделай.')

    def get_water_temperature(self):
        return str(self.min_water_temperature) + '-' + str(self.max_water_temperature)

    def if_added_water_temperature(self, min_water_temperature, max_water_temperature):
        if int(min_water_temperature) < 20 or int(min_water_temperature) > int(max_water_temperature):
            raise ValueError('Рыбка замёрзнет. Переделай.')
        elif int(max_water_temperature) > 28 or int(max_water_temperature) < int(min_water_temperature):
            raise ValueError('Рыбка запечётся. Переделай.')

    def get_hydrogen_index(self):
        return str(self.min_hydrogen_index) + '-' + str(self.max_hydrogen_index)

    def if_added_hydrogen_index(self, min_hydrogen_index, max_hydrogen_index):
        if float(min_hydrogen_index) < 7 or float(min_hydrogen_index) > float(max_hydrogen_index):
            raise ValueError('Маленький водородный показатель. Переделай.')
        elif float(max_hydrogen_index) > 8.5 or float(max_hydrogen_index) < float(min_hydrogen_index):
            raise ValueError('Большой водородный показатель. Переделай.')

    def get_water_hardness(self):
        return str(self.min_water_hardness) + '-' + str(self.max_water_hardness)

    def if_added_water_hardness(self, min_water_hardness, max_water_hardness):
        if int(min_water_hardness) < 5 or int(min_water_hardness) > int(max_water_hardness):
            raise ValueError('Слишком мягкая вода. Переделай.')
        elif int(max_water_hardness) > 30 or int(max_water_hardness) < int(max_water_hardness):
            raise ValueError('Слишком жёсткая вода. Переделай.')

    def __str__(self):
        return 'Семейство: ' + str(self.get_family()) + '\nМaxовый размер: ' + str(self.get_fish_size()) + ' см\nМинимальное количество литров: '\
               + str(self.get_min_number_of_liters()) + ' на пару\nТемпература воды: ' + str(self.get_water_temperature()) + '°С\nВодородный показатель: '\
               + str(self.get_hydrogen_index()) + '\nЖёсткость воды: ' + str(self.get_water_hardness())

    def write_to_file(self):
        return str(self.get_family()) + ',' + str(self.name) + ',' + str(self.get_fish_size()) + ',' + str(self.get_min_number_of_liters()) + ',' + \
               str(self.min_water_temperature) + ',' + str(self.max_water_temperature) + ',' + str(self.min_hydrogen_index) + ',' + \
               str(self.max_hydrogen_index) + ',' + str(self.min_water_hardness) + ',' + str(self.max_water_hardness)


class FrameFishCarp(FrameFish):

    def __init__(self, family, name, fish_size, min_number_of_liters, min_water_temperature, max_water_temperature,
                min_hydrogen_index, max_hydrogen_index, min_water_hardness, max_water_hardness):
        FrameFish.__init__(self, family, name, fish_size)

        self.if_added_min_number_of_liters(min_number_of_liters)
        self.min_number_of_liters = int(min_number_of_liters)

        self.if_added_water_temperature(min_water_temperature, max_water_temperature)
        self.min_water_temperature = int(min_water_temperature)
        self.max_water_temperature = int(max_water_temperature)

        self.if_added_hydrogen_index(min_hydrogen_index, max_hydrogen_index)
        self.min_hydrogen_index = float(min_hydrogen_index)
        self.max_hydrogen_index = float(max_hydrogen_index)

        self.if_added_water_hardness(min_water_hardness, max_water_hardness)
        self.min_water_hardness = int(min_water_hardness)
        self.max_water_hardness = int(max_water_hardness)

    def get_min_number_of_liters(self):
        return str(self.min_number_of_liters)

    def if_added_min_number_of_liters(self, min_number_of_liters):
        if int(min_number_of_liters) < 2:
            raise ValueError('Рыбка от сушника помрёт. Переделай.')

    def get_water_temperature(self):
        return str(self.min_water_temperature) + '-' + str(self.max_water_temperature)

    def if_added_water_temperature(self, min_water_temperature, max_water_temperature):
        if int(min_water_temperature) < 15 or int(min_water_temperature) > int(max_water_temperature):
            raise ValueError('Рыбка замёрзнет. Переделай.')
        elif int(max_water_temperature) > 28 or int(max_water_temperature) < int(min_water_temperature):
            raise ValueError('Рыбка запечётся. Переделай.')

    def get_hydrogen_index(self):
        return str(self.min_hydrogen_index) + '-' + str(self.max_hydrogen_index)

    def if_added_hydrogen_index(self, min_hydrogen_index, max_hydrogen_index):
        if float(min_hydrogen_index) < 5.5 or float(min_hydrogen_index) > float(max_hydrogen_index):
            raise ValueError('Маленький водородный показатель. Переделай.')
        elif float(max_hydrogen_index) > 8.5 or float(max_hydrogen_index) < float(min_hydrogen_index):
            raise ValueError('Большой водородный показатель. Переделай.')

    def get_water_hardness(self):
        return str(self.min_water_hardness) + '-' + str(self.max_water_hardness)

    def if_added_water_hardness(self, min_water_hardness, max_water_hardness):
        if int(min_water_hardness) < 0 or int(min_water_hardness) > int(max_water_hardness):
            raise ValueError('Слишком мягкая вода. Переделай.')
        elif int(max_water_hardness) > 20 or int(max_water_hardness) < int(max_water_hardness):
            raise ValueError('Слишком жёсткая вода. Переделай.')

    def __str__(self):
        return 'Семейство: ' + str(self.get_family()) + '\nМaxовый размер: ' + str(self.get_fish_size()) + ' см\nМинимальное количество литров: '\
               + str(self.get_min_number_of_liters()) + ' на пару\nТемпература воды: ' + str(self.get_water_temperature()) + '°С\nВодородный показатель: '\
               + str(self.get_hydrogen_index()) + '\nЖёсткость воды: ' + str(self.get_water_hardness())

    def write_to_file(self):
        return str(self.get_family()) + ',' + str(self.name) + ',' + str(self.get_fish_size()) + ',' + str(self.get_min_number_of_liters()) + ',' + \
               str(self.min_water_temperature) + ',' + str(self.max_water_temperature) + ',' + str(self.min_hydrogen_index) + ',' + \
               str(self.max_hydrogen_index) + ',' + str(self.min_water_hardness) + ',' + str(self.max_water_hardness)


class FrameFishGoldfish(FrameFish):

    def __init__(self, family, name, fish_size, min_number_of_liters, min_water_temperature, max_water_temperature,
                min_hydrogen_index, max_hydrogen_index, min_water_hardness, max_water_hardness):
        FrameFish.__init__(self, family, name, fish_size)

        self.if_added_min_number_of_liters(min_number_of_liters)
        self.min_number_of_liters = int(min_number_of_liters)

        self.if_added_water_temperature(min_water_temperature, max_water_temperature)
        self.min_water_temperature = int(min_water_temperature)
        self.max_water_temperature = int(max_water_temperature)

        self.if_added_hydrogen_index(min_hydrogen_index, max_hydrogen_index)
        self.min_hydrogen_index = float(min_hydrogen_index)
        self.max_hydrogen_index = float(max_hydrogen_index)

        self.if_added_water_hardness(min_water_hardness, max_water_hardness)
        self.min_water_hardness = int(min_water_hardness)
        self.max_water_hardness = int(max_water_hardness)

    def get_min_number_of_liters(self):
        return str(self.min_number_of_liters)

    def if_added_min_number_of_liters(self, min_number_of_liters):
        if int(min_number_of_liters) < 100:
            raise ValueError('Рыбка от сушника помрёт. Переделай.')

    def get_water_temperature(self):
        return str(self.min_water_temperature) + '-' + str(self.max_water_temperature)

    def if_added_water_temperature(self, min_water_temperature, max_water_temperature):
        if int(min_water_temperature) < 14 or int(min_water_temperature) > int(max_water_temperature):
            raise ValueError('Рыбка замёрзнет. Переделай.')
        elif int(max_water_temperature) > 30 or int(max_water_temperature) < int(min_water_temperature):
            raise ValueError('Рыбка запечётся. Переделай.')

    def get_hydrogen_index(self):
        return str(self.min_hydrogen_index) + '-' + str(self.max_hydrogen_index)

    def if_added_hydrogen_index(self, min_hydrogen_index, max_hydrogen_index):
        if float(min_hydrogen_index) < 6 or float(min_hydrogen_index) > float(max_hydrogen_index):
            raise ValueError('Маленький водородный показатель. Переделай.')
        elif float(max_hydrogen_index) > 8 or float(max_hydrogen_index) < float(min_hydrogen_index):
            raise ValueError('Большой водородный показатель. Переделай.')

    def get_water_hardness(self):
        return str(self.min_water_hardness) + '-' + str(self.max_water_hardness)

    def if_added_water_hardness(self, min_water_hardness, max_water_hardness):
        if int(min_water_hardness) < 0 or int(min_water_hardness) > int(max_water_hardness):
            raise ValueError('Слишком мягкая вода. Переделай.')
        elif int(max_water_hardness) > 20 or int(max_water_hardness) < int(max_water_hardness):
            raise ValueError('Слишком жёсткая вода. Переделай.')

    def __str__(self):
        return 'Семейство: ' + str(self.get_family()) + '\nМaxовый размер: ' + str(self.get_fish_size()) + ' см\nМинимальное количество литров: '\
               + str(self.get_min_number_of_liters()) + ' на пару\nТемпература воды: ' + str(self.get_water_temperature()) + '°С\nВодородный показатель: '\
               + str(self.get_hydrogen_index()) + '\nЖёсткость воды: ' + str(self.get_water_hardness())

    def write_to_file(self):
        return str(self.get_family()) + ',' + str(self.name) + ',' + str(self.get_fish_size()) + ',' + str(self.get_min_number_of_liters()) + ',' + \
               str(self.min_water_temperature) + ',' + str(self.max_water_temperature) + ',' + str(self.min_hydrogen_index) + ',' + \
               str(self.max_hydrogen_index) + ',' + str(self.min_water_hardness) + ',' + str(self.max_water_hardness)


def read_data(frame_mas):
    with open('data.txt') as file:
        for line in file.readlines():
            if len(line) > 0:
                new_data = line.split(',')
                if new_data[0] == 'живородящие':
                    frame_mas.append(FrameFishViviparous(new_data[0], new_data[1], new_data[2], new_data[3], new_data[4],
                                                         new_data[5], new_data[6], new_data[7], new_data[8], new_data[9]))
                if new_data[0] == 'карповые и карпозубые':
                    frame_mas.append(FrameFishCarp(new_data[0], new_data[1], new_data[2], new_data[3], new_data[4],
                                                         new_data[5], new_data[6], new_data[7], new_data[8], new_data[9]))
                if new_data[0] == 'золотая рыбка':
                    frame_mas.append(FrameFishGoldfish(new_data[0], new_data[1], new_data[2], new_data[3], new_data[4],
                                                         new_data[5], new_data[6], new_data[7], new_data[8], new_data[9]))
    return frame_mas


def save_data():
    with open('data.txt', 'w') as file:
        for fr in frame_mas:
            file.write(fr.write_to_file() + ',\n')


frame_mas = []
read_data(frame_mas)
while True:
    option = int(input('Что хочешь сделать?\n1)Добавить рыбку\n2)Вывести досье рыбки\n3)Удалить рыбку\n'))
    if option == 1:
        new_fish_family = ''
        while new_fish_family not in ['живородящие', 'карповые и карпозубые', 'золотая рыбка']:
            new_fish_family = input('Введите название семейства(живородящие, карповые и карпозубые, золотая рыбка):')
        new_fish_name = input('Введите название рыбки: ')
        new_fish_size = input('Введите мaxовый размер рыбки: ')
        new_min_number_of_liters = input('Введите минимальное количество литров: ')
        new_min_water_temperature = input('Введите минимальную температуру воды: ')
        new_max_water_temperature = input('Введите максимальную температуру воды: ')
        new_min_hydrogen_index = input('Введите минимальный водородный показатель: ')
        new_max_hydrogen_index = input('Введите максимальный водородный показатель: ')
        new_min_water_hardness = input('Введите минимальную жёсткость воды: ')
        new_max_water_hardness = input('Введите максимальную жёсткость воды: ')
        if new_fish_family == 'живородящие':
            try:
                frame_mas.append(FrameFishViviparous(new_fish_family, new_fish_name, new_fish_size, new_min_number_of_liters, new_min_water_temperature, new_max_water_temperature, new_min_hydrogen_index, new_max_hydrogen_index, new_min_water_hardness, new_max_water_hardness))
            except ValueError as e:
                print(e)
        elif new_fish_family == 'карповые и карпозубые':
            try:
                frame_mas.append(FrameFishCarp(new_fish_family, new_fish_name, new_fish_size, new_min_number_of_liters, new_min_water_temperature, new_max_water_temperature, new_min_hydrogen_index, new_max_hydrogen_index, new_min_water_hardness, new_max_water_hardness))
            except ValueError as e:
                print(e)
        elif new_fish_family == 'золотая рыбка':
            try:
                frame_mas.append(FrameFishGoldfish(new_fish_family, new_fish_name, new_fish_size, new_min_number_of_liters, new_min_water_temperature, new_max_water_temperature, new_min_hydrogen_index, new_max_hydrogen_index, new_min_water_hardness, new_max_water_hardness))
            except ValueError as e:
                print(e)
        save_data()
    elif option == 2:
        find_fish_name = input('Введите название рыбки: ')
        for fish in frame_mas:
            if fish.name == find_fish_name:
                print(fish)
    elif option == 3:
        delete_fish_name = input('Введите название рыбки: ')
        for fish in frame_mas:
            if fish.name == delete_fish_name:
                frame_mas.remove(fish)
        save_data()
