import json
import graphviz

#начальная базы правил, в программе загружается из baza.json
rules = [
    {'conditions': [{'интенсивность цветения': 'один'}, {'сезон': 'летний'}], 'conclusion': {'тип цветкового растения': 'летний-однолетний'}},
    {'conditions': [{'интенсивность цветения': 'один'}, {'сезон': 'весений'}], 'conclusion': {'тип цветкового растения': 'весений-однолетний'}},
    {'conditions': [{'интенсивность цветения': 'более'}, {'сезон': 'летний'}], 'conclusion': {'тип цветкового растения': 'летний-многолетний'}},
    {'conditions': [{'интенсивность цветения': 'более'}, {'сезон': 'весений'}], 'conclusion': {'тип цветкового растения': 'весений-многолетний'}},
    {'conditions': [{'тип цветкового растения': 'летний-многолетний'}, {'аромат': 'сильный'}, {'цвет': 'красный'}], 'conclusion': {'цветок': 'Роза'}},
    {'conditions': [{'тип цветкового растения': 'летний-многолетний'}, {'аромат': 'сильный'}, {'цвет': 'фиолетовый'}], 'conclusion': {'цветок': 'Лаванда'}},
    {'conditions': [{'тип цветкового растения': 'летний-однолетний'}, {'аромат': 'нету'}, {'цвет': 'белый'}], 'conclusion': {'цветок': 'Маргаритка'}},
    {'conditions': [{'тип цветкового растения': 'весений-однолетний'}, {'аромат': 'слабый'}, {'цвет': 'белый'}], 'conclusion': {'цветок': 'Ирис'}},
]

#сохранение базы правил в память
def save_rules_to_file(rules):
    with open('baza.json', 'w') as f:
        json.dump(rules, f)

#загрузка базы правил
def load_rules_from_file():
    with open('baza.json', 'r') as f:
        rules = json.load(f)
    return rules

def getFlower(db, rules, graph):
    counter = 0
    last_node = -1
    #мы последовательно проходим по каждому правилу и внутри правила проходим по условиям,
    # если количество совпавших условий = количеству условий значит мы нашли требуемое правило и можем сделать вывод
    for rule in rules:
        conditions = rule['conditions']
        matches = 0
        for condition in conditions:
            key = next(iter(condition))
            value = condition[key]
            if db[key] == value:
                matches += 1

        #код создания графов, если есть хоть 1 совпадение то добавляем правило 
        if matches > 0:
            graph.node(str(counter), label= str(conditions))
            counter += 1
        if last_node >= 0 and matches > 0:
            graph.edge(str(last_node), str(counter-1))
        # elif last_node >= 0:    
        #     graph.edge(str(last_node), str(counter-1))

        # если количество совпавших условий = количеству условий, значит мы нашли требуемое правило и можем сделать вывод о сложности и обновить рабочую область
        if matches == len(conditions):
            last_node = counter - 1
            db.update(rule['conclusion'])
            if (db['цветок'] != None):
                last_node = counter - 1
                return db, last_node

    return db, last_node

# save_rules_to_file(rules)
rules = load_rules_from_file()

while True:
    graph = graphviz.Digraph()
    scent, flowering_rate, color, season = "", "", "", ""

    print("Здравствуйте! Подобрать вам цветок?(Да/Нет)")
    hello = input()
    if (hello == 'Нет'):
            exit()
    elif (hello != "Да"): exit() 
    
    print("Цикл растения должен быть больше года?(Да/Нет)")
    answer = input()
    if (answer == "Да"): flowering_rate = "более"
    else: flowering_rate = "один"
    print("Растение должен иметь аромат?(Да/Нет)")
    answer = input()
    if (answer == "Да"):
        print("Аромат должен быть яркий?(Да/Нет)")
        answer = input()
        if (answer == 'Да'): scent = 'сильный'
        else: scent = 'слабый'
    else: scent = "нету"
    print("В какой сезон должен цвести? (весений/летний/осений)")
    answer = input()
    season = answer
    print("Какой цвет должен иметь цветок? (красный/белый/фиолетовый)")
    answer = input()
    color = answer


    # факты о странице, которые вводит пользователь
    # он же - глобальная база данных
    db = {
        'аромат': scent,
        'цвет': color,
        'интенсивность цветения': flowering_rate,
        'сезон': season,
        'тип цветкового растения': None,
        'цветок': None
    }

    complete, last_node = getFlower(db,rules,graph)

    #если не нашли нужное правило - предложить добавить 
    if (complete['цветок'] == None):
        print("Конфигурация не найдена, хотите добавить?(Да/Нет)")
        answer = input()
        if (answer != "Да"): 
            print("Конфигурация не будет добавлена")
            exit()
        else:
            if (complete['тип цветкового растения'] == None ):
                print('Введите тип цветкового растения (Например, "осений-многолетний")')
                complexity = str(input())
                new_rule = {'conditions': [{'интенсивность цветения': flowering_rate}, {'сезон': season}], 'conclusion': {'тип цветкового растения': complexity}}
                rules.append(new_rule)
                save_rules_to_file(rules)
                print('База знаний обновлена')
            else:
                print('Введите названия цветка для этих данных')
                flower = str(input())
                new_rule = {'conditions': [{'тип цветкового растения': db['тип цветкового растения']}, {'аромат': scent}, {'цвет': color}], 'conclusion': {'цветок': flower}}
                rules.append(new_rule)
                save_rules_to_file(rules)
                print('База знаний обновлена')
    else:
        output = complete['цветок']
        print(f'Вам подойдет цветок: {output}')
        graph.node('result', label= 'цветок\n' + str(complete['цветок']))
        graph.edge(str(last_node),'result')
        # выводим граф
        graph.render('graph')
        graph.view()