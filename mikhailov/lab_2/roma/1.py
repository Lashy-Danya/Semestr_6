# Python 3.9
# Needed libraries are below
import graphviz

fish_size = -1
min_number_of_liters = -1
water_temperature = -1
hydrogen_index = -1
water_hardness = -1
data_base = [-1, 1, -1, -1, -1, 'Это гуппи',
             -1, -1, 4, -1, -1, 'Это гуппи',
             -1, 4, -1, -1, -1, 'Это меченосец',
             2, -1, 1, -1, -1, 'Это меченосец',
             3, -1, 2, -1, -1, 'Это моллинезия "красный леопард"',
             -1, 5, -1, 2, 3, 'Это моллинезия "красный леопард"',
             5, -1, -1, -1, -1, 'Это моллинезия парусная велифера',
             4, -1, -1, -1, -1, 'Это моллинезия серебряная (Снежинка)',
             2, 5, -1, -1, -1, 'Это моллиенезия сфенопс',
             2, -1, 3, -1, -1, 'Это моллиенезия сфенопс',
             2, -1, -1, -1, 4, 'Это моллиенезия сфенопс',
             -1, 5, -1, 1, -1, 'Это моллиенезия сфенопс',
             -1, -1, 4, 1, -1, 'Это моллиенезия сфенопс',
             -1, -1, -1, 1, 4, 'Это моллиенезия сфенопс',
             3, -1, 3, -1, -1, 'Это моллинезия черная',
             3, -1, -1, -1, 4, 'Это моллинезия черная',
             -1, 3, -1, -1, -1, 'Это номорамфус Лима',
             -1, -1, -1, -1, 1, 'Это номорамфус Лима',
             2, -1, 2, -1, -1, 'Это номорамфус Лима',
             2, -1, -1, 2, -1, 'Это номорамфус Лима',
             -1, 2, -1, -1, -1, 'Это пецилия',
             1, -1, 1, -1, -1, 'Это пецилия',
             1, -1, -1, 1, -1, 'Это пецилия']
keep_writing = 1
otvet = 0
answer = 'Д'
dot = graphviz.Digraph(name='буль-буль')

while answer == 'Д':
    print('Хотите добавить новую рыбку и правила для её выбора в базу данных?(Д/Н)')
    answer = input()
    if answer == 'Д':
        temp_fish_size = -1
        temp_min_number_of_liters = -1
        temp_water_temperature = -1
        temp_hydrogen_index = -1
        temp_water_hardness = -1
        fish_name = input('Как называется новая рыбка?\n')
        exit_condition = 1
        while(exit_condition):
            param = input('Какой параметр меняем?\n1)Max-ый размер рыбки    2)Min-ое кол-во литров    3)Т°С воды    4)рН воды    5)dН° воды\n')
            if int(param) == 1:
                temp_fish_size = input('Выберите новое значение Max-ый размер рыбки\n'
                                       '1)6 см    2)10 см    3)12 см    4)14 см    5)15 см\n')
            elif int(param) == 2:
                temp_min_number_of_liters = input('Выберите новое значение Min-ое кол-во литров\n'
                                                  '1)5 на пару    2)15 на пару    3)20 на пару    4)30 на пару    5)50 на пару    6)60 на пару\n')
            elif int(param) == 3:
                temp_water_temperature = input('Выберите новое значение Т°С воды\n'
                                               '1)20-26    2)22-28    3)23-28    4)24-26\n')
            elif int(param) == 4:
                temp_hydrogen_index = input('Выберите новое значение рН воды\n'
                                            '1)7-8    2)7-8,5\n')
            elif int(param) == 5:
                temp_water_hardness = input('Выберите новое значение dН° воды\n'
                                            '1)5-25    2)8-25    3)10-25    4)10-30\n')
            answer1 = input('Какое условие?(И/ИЛИ/КОНЕЦ)')
            if answer1 == 'ИЛИ' or answer1 == 'КОНЕЦ':
                data_base.append(int(temp_fish_size))
                data_base.append(int(temp_min_number_of_liters))
                data_base.append(int(temp_water_temperature))
                data_base.append(int(temp_hydrogen_index))
                data_base.append(int(temp_water_hardness))
                data_base.append('Это ' + fish_name)
                temp_fish_size = -1
                temp_min_number_of_liters = -1
                temp_water_temperature = -1
                temp_hydrogen_index = -1
                temp_water_hardness = -1
                if answer1 == 'КОНЕЦ':
                    exit_condition = 0
    elif answer == 'Н':
        break

print('Определяем какие рыбки могут жить у вас в аквариуме. Просто введите цифру того параметра, который '
      'соответствует вашему аквариуму или рыбке, которую хотите в нём держать.'
      '\nКак введёте все извеcтные параметры '
      'введите знак \'!\' и ввод завершиться. Ввод так же завершиться, когда вы введёте все параметры.\n')
while(keep_writing):
    print('{:>25}'.format('Max-ый размер рыбки') + '|' + '{:>25}'.format('Min-ое кол-во литров') + '|' + '{:>20}'.format('Т°С воды') + '|' +
          '{:>20}'.format('рН воды') + '|' + '{:>20}'.format('dН° воды') + '\n'
          '------------------------------------------------------------------------------------------------------------'
          '------\n' +
          '{:>25}'.format('11) 6 см') + '|' + '{:>25}'.format('21) 5 на пару') + '|' + '{:>20}'.format('31)20-26') + '|' +
          '{:>20}'.format('41)  7-8') + '|' + '{:>20}'.format('51) 5-25') + '\n' +
          '{:>25}'.format('12)10 см') + '|' + '{:>25}'.format('22)15 на пару') + '|' + '{:>20}'.format('32)22-28') + '|' +
          '{:>20}'.format('42)7-8,5') + '|' + '{:>20}'.format('52) 8-25') + '\n' +
          '{:>25}'.format('13)12 см') + '|' + '{:>25}'.format('23)20 на пару') + '|' + '{:>20}'.format('33)23-28') + '|' +
          '{:>20}'.format(' ') + '|' + '{:>20}'.format('53)10-25') + '\n' +
          '{:>25}'.format('14)14 см') + '|' + '{:>25}'.format('24)30 на пару') + '|' + '{:>20}'.format('34)24-26') + '|' +
          '{:>20}'.format(' ') + '|' + '{:>20}'.format('54)10-30') + '\n' +
          '{:>25}'.format('15)15 см') + '|' + '{:>25}'.format('25)50 на пару') + '|' + '{:>20}'.format(' ') + '|' +
          '{:>20}'.format(' ') + '|' + '{:>20}'.format(' ') + '\n' +
          '{:>25}'.format(' ') + '|' + '{:>25}'.format('26)60 на пару') + '|' + '{:>20}'.format(' ') + '|' +
          '{:>20}'.format(' ') + '|' + '{:>20}'.format(' ') + '\n')
    otvet = input('Ответ:')
    if otvet == '!':
        keep_writing = 0
    elif int(otvet) > 10 and int(otvet) < 20:
        if int(otvet) == 11: # 6 см
            fish_size = 1
        elif int(otvet) == 12: # 10 см
            fish_size = 2
        elif int(otvet) == 13: # 12 см
            fish_size = 3
        elif int(otvet) == 14: # 14 см
            fish_size = 4
        elif int(otvet) == 15: # 15 см
            fish_size = 5
    elif int(otvet) > 20 and int(otvet) < 30:
        if int(otvet) == 21: # 5 на пару
            min_number_of_liters = 1
        elif int(otvet) == 22: # 15 на пару
            min_number_of_liters = 2
        elif int(otvet) == 23: # 20 на пару
            min_number_of_liters = 3
        elif int(otvet) == 24: # 30 на пару
            min_number_of_liters = 4
        elif int(otvet) == 25: # 50 на пару
            min_number_of_liters = 5
        elif int(otvet) == 26: # 60 на пару
            min_number_of_liters = 6
    elif int(otvet) > 30 and int(otvet) < 40:
        if int(otvet) == 31: # 20-26
            water_temperature = 1
        elif int(otvet) == 32: # 22-28
            water_temperature = 2
        elif int(otvet) == 33: # 23-28
            water_temperature = 3
        elif int(otvet) == 34: # 24-26
            water_temperature = 4
    elif int(otvet) > 40 and int(otvet) < 50:
        if int(otvet) == 41: # 7-8
            hydrogen_index = 1
        elif int(otvet) == 42: # 7-8,5
            hydrogen_index = 2
    elif int(otvet) > 50 and int(otvet) < 60:
        if int(otvet) == 51: # 5-25
            water_hardness = 1
        elif int(otvet) == 52: # 8-25
            water_hardness = 2
        elif int(otvet) == 53: # 10-25
            water_hardness = 3
        elif int(otvet) == 54: # 10-30
            water_hardness = 4
    if fish_size != -1 and min_number_of_liters != -1 and water_temperature != -1 and hydrogen_index != -1 and water_hardness != -1:
        keep_writing = 0
if fish_size == -1 and min_number_of_liters == -1 and water_temperature == -1 and hydrogen_index == -1 and water_hardness == -1:
    print('Вы ничего не ввели и я не могу ничего определить')
    exit()
else:
    solution = int(0)
    score = int(2)
    i = int(0)
    while i < len(data_base):
        if data_base[i] == fish_size and data_base[i + 1] == min_number_of_liters  and data_base[i + 2] == water_temperature and data_base[i + 3] == hydrogen_index and data_base[i + 4] == water_hardness:
            solution = data_base[i + 5]
            dot.node('1', solution)
            print(solution)
            break
        i = i + 6
    if solution == 0:
        print('Ничего конкретного определить не получилось')
    i = int(0)
    while i < len(data_base):
        if data_base[i + 5] == solution:
            how_much = int(1)
            if data_base[i] != -1:
                if data_base[i] == 1:
                    dot.node(str(score), 'Max-ый размер рыбки\n 6 см')
                elif data_base[i] == 2:
                    dot.node(str(score), 'Max-ый размер рыбки\n 10 см')
                elif data_base[i] == 3:
                    dot.node(str(score), 'Max-ый размер рыбки\n 12 см')
                elif data_base[i] == 4:
                    dot.node(str(score), 'Max-ый размер рыбки\n 14 см')
                elif data_base[i] == 5:
                    dot.node(str(score), 'Max-ый размер рыбки\n 15 см')
                dot.edge(str(score), '1')
                score = int(score) + 1
                how_much = how_much + 1
            if data_base[i + 1] != -1:
                if data_base[i + 1] == 1:
                    dot.node(str(score), 'Min-ое кол-во литров\n 5 на пару')
                if data_base[i + 1] == 2:
                    dot.node(str(score), 'Min-ое кол-во литров\n 15 на пару')
                if data_base[i + 1] == 3:
                    dot.node(str(score), 'Min-ое кол-во литров\n 20 на пару')
                if data_base[i + 1] == 4:
                    dot.node(str(score), 'Min-ое кол-во литров\n 30 на пару')
                if data_base[i + 1] == 5:
                    dot.node(str(score), 'Min-ое кол-во литров\n 50 на пару')
                if data_base[i + 1] == 6:
                    dot.node(str(score), 'Min-ое кол-во литров\n 60 на пару')
                dot.edge(str(score), '1')
                for j in range(1, how_much):
                    dot.edge(str(score - j), str(score), constraint='false', arrowhead='none')
                score = int(score) + 1
                how_much = how_much + 1
            if data_base[i + 2] != -1:
                if data_base[i + 2] == 1:
                    dot.node(str(score), 'Т°С воды\n 20-26')
                if data_base[i + 2] == 2:
                    dot.node(str(score), 'Т°С воды\n 22-28')
                if data_base[i + 2] == 3:
                    dot.node(str(score), 'Т°С воды\n 23-28')
                if data_base[i + 2] == 4:
                    dot.node(str(score), 'Т°С воды\n 24-26')
                dot.edge(str(score), '1')
                for j in range(1, how_much):
                    dot.edge(str(score - j), str(score), constraint='false', arrowhead='none')
                score = int(score) + 1
                how_much = how_much + 1
            if data_base[i + 3] != -1:
                if data_base[i + 3] == 1:
                    dot.node(str(score), 'рН воды\n 7-8')
                if data_base[i + 3] == 2:
                    dot.node(str(score), 'рН воды\n 7-8,5')
                dot.edge(str(score), '1')
                for j in range(1, how_much):
                    dot.edge(str(score - j), str(score), constraint='false', arrowhead='none')
                score = int(score) + 1
                how_much = how_much + 1
            if data_base[i + 4] != -1:
                if data_base[i + 4] == 1:
                    dot.node(str(score), 'dН° воды\n 5-25')
                if data_base[i + 4] == 2:
                    dot.node(str(score), 'dН° воды\n 8-25')
                if data_base[i + 4] == 3:
                    dot.node(str(score), 'dН° воды\n 10-25')
                if data_base[i + 4] == 4:
                    dot.node(str(score), 'dН° воды\n 10-30')
                dot.edge(str(score), '1')
                for j in range(1, how_much):
                    dot.edge(str(score - j), str(score), constraint='false', arrowhead='none')
                score = int(score) + 1
                how_much = how_much + 1
        i = i + 6
    dot.render('test-table', view=True)
