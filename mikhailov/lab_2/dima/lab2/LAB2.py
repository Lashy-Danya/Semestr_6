import json
import graphviz

#начальная базы правил, в программе загружается из baza.json
rules = [
    {'conditions': [{'дизайн': 'простой'}, {'контент': 'мало'}], 'conclusion': {'уровень сложности': 'Легкий'}},
    {'conditions': [{'дизайн': 'простой'}, {'контент': 'много'}], 'conclusion': {'уровень сложности': 'Средний'}},
    {'conditions': [{'дизайн': 'сложный'}, {'контент': 'мало'}], 'conclusion': {'уровень сложности': 'Средний'}},
    {'conditions': [{'дизайн': 'сложный'}, {'контент': 'много'}], 'conclusion': {'уровень сложности': 'Сложный'}},
    {'conditions': [{'уровень сложности': 'Легкий'}, {'анимация': 'нет'}], 'conclusion': {'цена': 'Низкая'}},
    {'conditions': [{'уровень сложности': 'Легкий'}, {'анимация': 'есть'}], 'conclusion': {'цена': 'Средняя'}},
    {'conditions': [{'уровень сложности': 'Средний'}, {'анимация': 'нет'}], 'conclusion': {'цена': 'Средняя'}},
    {'conditions': [{'уровень сложности': 'Средний'}, {'анимация': 'есть'}], 'conclusion': {'цена': 'Высокая'}},
    {'conditions': [{'уровень сложности': 'Сложный'}, {'анимация': 'есть'}], 'conclusion': {'цена': 'Очень высокая'}}
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

#функция получениия цены на основе заданных условий
#интерпретатор правил - функция логического вывода
def getPrice(db, rules, graph):
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
            if (db['цена'] != None):
                last_node = counter - 1
                return db, last_node

        
    
    return db, last_node

#Функция добавления
def addRule(rules):
    design, animations, content = "", "", ""
    print("Добавление правила")
    print("Добавление правила сложности или цены?(1/2)")
    answer = str(input())
    if answer == '1':
        print("Должен сайт иметь сложный дизайн?(Да/Нет)")
        answer = input()
        if (answer == "Да"): design = "сложный"
        else: design = "простой"
        print("Должен сайт иметь много контента?(Да/Нет)")
        answer = input()
        if (answer == "Да"): content = "много"
        else: content = "мало"
        print("Как вы оцените сложность конфигурации - Легкий, Средний, Сложный?")
        complexity = str(input())
        new_rule = {'conditions': [{'дизайн': design}, {'контент': content}], 'conclusion': {'уровень сложности': complexity}}
        rules.append(new_rule)
        save_rules_to_file(rules)
    elif answer == '2':
        print("Какую сложность должен иметь сайт?(Легкий/Средний/Сложный)")
        complexity = str(input())
        print("Должен сайт иметь много анимацию?(Да/Нет)")
        answer = input()
        if (answer == "Да"): animations = "есть"
        else: animations = "нет"
        print("Как вы оцените стоимость данной конфигурации?")
        price = str(input())
        new_rule = {'conditions': [{'уровень сложности': complexity}, {'анимация': animations}], 'conclusion': {'цена': price}}
        rules.append(new_rule)
        save_rules_to_file(rules)
        print('База знаний обновлена')
    


#save_rules_to_file(rules)
rules = load_rules_from_file()

while True:
    graph = graphviz.Digraph()
    design, animations, content = "", "", ""

    print("Здравствуйте! Вы хотите оценить стоимость сайта?(Да/Нет)")
    hello = input()
    if (hello == 'Нет'):
            print("Добавить новое правило?(Да/Нет)")
            hello2 = input()
            if(hello2 != "Да"): exit() 
            else:
                addRule(rules)
                continue
    elif (hello != "Да"): exit() 
    
    print("Должен сайт иметь качественную анимацию?(Да/Нет)")
    answer = input()
    if (answer == "Да"): animations = "есть"
    else: animations = "нет"
    print("Должен сайт иметь сложный дизайн?(Да/Нет)")
    answer = input()
    if (answer == "Да"): design = "сложный"
    else: design = "простой"
    print("Должен сайт иметь много контента?(Да/Нет)")
    answer = input()
    if (answer == "Да"): content = "много"
    else: content = "мало"


    # факты о странице, которые вводит пользователь
    # он же - глобальная база данных
    db = {
        'дизайн': design,
        'контент': content,
        'анимация': animations,
        'уровень сложности': None,
        'цена': None
    }

    complete, last_node = getPrice(db,rules,graph)

    #если не нашли нужное правило - предложить добавить 
    if (complete['цена'] == None):
        print("Конфигурация не найдена, хотите добавить?(Да/Нет)")
        answer = input()
        if (answer != "Да"): 
            print("Конфигурация не будет добавлена")
            exit()
        else:
            if (complete['уровень сложности'] == None ):
                print('Введите сложность по результатам контента и дизайна - Легкий, Средний, Сложный')
                complexity = str(input())
                new_rule = {'conditions': [{'дизайн': design}, {'контент': content}], 'conclusion': {'уровень сложности': complexity}}
                rules.append(new_rule)
                save_rules_to_file(rules)
                print('База знаний обновлена')
            else:
                print('Введите цену для этой сборки - Очень низкая, Низкая, Средняя, Высокая, Очень высокая')
                price = str(input())
                new_rule = {'conditions': [{'уровень сложности': db['уровень сложности']}, {'анимация': animations}], 'conclusion': {'цена': price}}
                rules.append(new_rule)
                save_rules_to_file(rules)
                print('База знаний обновлена')
    else:
        output = complete['цена']
        print(f'Стоимость разработки страницы: {output}')
        graph.node('result', label= 'цена\n' + str(complete['цена']))
        graph.edge(str(last_node),'result')
        # выводим граф
        graph.render('graph')
        graph.view()