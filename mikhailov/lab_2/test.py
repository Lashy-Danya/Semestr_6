import copy

# Функция возвращает строку с правилом в формате: ЕСЛИ условие, ТО действие
def rule_repr(rule):
    LHS = []
    for attr, values in rule['LHS'].items():
        LHS.append(attr + " = " + "|".join(values))
    (RHSkey, RHSvalue) = list(rule['RHS'].items())[0]
    return "IF " + " & ".join(LHS) + " THEN " + RHSkey + " = " + RHSvalue

# получение данных из базы знаний
def parse(path):
    parameters = {}
    rules = []
    try:
        with open(path, 'r') as f:
            lines = f.readlines()
    except:
        print("Problem with open file " + path)
        return

    for line in lines:
        if not line or line.startswith('-') or line.startswith('#'):
            continue
        elif line.startswith('IF'):
            current = {}
            sides = line.replace('IF', '').split('THEN')
            current['LHS'] = {}

            conditions = sides[0].split('&')
            for condition in conditions:
                HS = list(map(str.strip, condition.split('=', 1)))
                current['LHS'][HS[0]] = [s.strip() for s in HS[1].split('|')]

            action = sides[1]
            HS = list(map(str.strip, action.split('=')))
            current['RHS'] = {HS[0]: HS[1]}
            rules.append(copy.deepcopy(current))
        else:
            splitLine = line.split('=', 1)
            parameters[splitLine[0].strip()] = [s.strip()
                                                for s in splitLine[1].split('|')]
    return parameters, rules

# Функция печатает рабочую память
def printRM():
    print("Введенные значения атрибутов:")
    for r, v in RM.items():
        print(r, " = ", v)

# Функция возвращает список правил правая часть которых значение параметра
def getConflictRules(rules, goal):
    ruleset = []
    for rule in rules:
        attribute = list(rule['RHS'].keys())[0]
        if attribute == goal:
            ruleset.append(rule)
    return ruleset

# Функция проверяет, существует ли хотя бы одно правило, правая часть которого является значением цели.
def conflictRuleExists(rules, goal):
    for rule in rules:
        attribute = list(rule['RHS'].keys())[0]
        if attribute == goal:
            return True
    return False

# Функция проверяет необходимое ли это правило
def ruleWorks(rule, RM):
    conditions = rule['LHS']

    for param in conditions:
        if param in RM:
            if RM[param] not in conditions[param]:
                return False
        else:
            return False
    return True

# Функция, позволяющая пользователю ввести параметр по умолчанию в рабочую память.
def parameterInput(param, RM):
    value = input("Введите значение параметра '" + param +
                  "' " + str(parameters[param+"*"]) + ": ")
    while(value not in parameters[param+"*"]):
        value = input()
    RM[param] = value

# Функция печатает атрибуты / параметры, их значения и все правила, содержащиеся в БЗ
def printKnowledgeBase(parameters, rules):
    print('-'*150)
    print("Атрибуты:")
    for attr, value in parameters.items():
        print(attr + " = " + " | ".join(value))

    print("\nПравила:")
    for i, rule in enumerate(rules):
        print(str(i+1) + ") " + rule_repr(rule))

    print('-'*150 + '\n')

# Получить атрибуты и правила из базы знаний
parameters, rules = parse('./Data.txt')
printKnowledgeBase(parameters, rules)

# Рабочая память, стек с целями и список уже проверенных атрибутов
RM = {}
goals = []
checked_goals = []

# Просит пользователя ввести целевую гипотезу
goal = input('Введите "Цветок" для начала работы: ')
goals.append(goal)

while(True):
    if len(goals) == 0:
        break
    new_goal = False
    new_parameter = False
    goal = goals[-1]
    conflictRules = getConflictRules(rules, goal)
    remainingRules = len(conflictRules)
    if remainingRules == 0:
        print('В базе знаний нет информации об этом цветке.')
        break
    print('Правила: ')
    for cr in conflictRules:
        print(rule_repr(cr))
    printRM()
    for cr in conflictRules:
        if ruleWorks(cr, RM):
            (RHSkey, RHSvalue) = list(cr['RHS'].items())[0]
            RM[RHSkey] = RHSvalue
            curr_goal = goals.pop()
            print("Результат: " + curr_goal + " = " + RHSvalue)
            new_goal = True
            break
    if new_goal:
        continue
    for cr in conflictRules:
        if new_goal:
            break
        remainingRules -= 1
        conditions = cr['LHS']
        for param in conditions:
            if param in checked_goals:
                break
            if param in RM:
                if RM[param] not in conditions[param]:
                    break
            else:  
                if conflictRuleExists(rules, param):
                    goals.append(param)
                    new_goal = True
                    break
                elif param + "*" in parameters:
                    parameterInput(param, RM)
                    new_parameter = True
                    break
                else:
                    checked_goals.append(param)
        if new_parameter:
            break
        if remainingRules == 0 and not new_goal:
            curr_goal = goals.pop()
            checked_goals.append(curr_goal)
            print('В базе знаний нет информации об этом цветке.')
    print('-'*150)
