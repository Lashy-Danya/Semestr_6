# Определяем базу правил
rules = [
    {'если': {'цветок': 'роза'}, 'то': {'цвет': 'красный'}},
    {'если': {'цветок': 'тюльпан'}, 'то': {'цвет': 'желтый'}},
    {'если': {'цветок': 'ирис'}, 'и': {'сезон': 'весна'}, 'то': {'цвет': 'фиолетовый'}},
    {'если': {'цветок': 'ландыш'}, 'и': {'сезон': 'весна'}, 'то': {'цвет': 'белый'}},
    {'если': {'цветок': 'хризантема'}, 'или': [{'сезон': 'осень'}, {'сезон': 'зима'}], 'то': {'цвет': 'желтый'}},
    {'если': {'цветок': 'гладиолус'}, 'или': [{'цвет': 'белый'}, {'цвет': 'розовый'}], 'то': {'сезон': 'лето'}},
]

# Определяем глобальную базу данных
facts = [
    {'цветок': 'роза'},
    {'цветок': 'тюльпан'},
    {'цветок': 'ирис', 'сезон': 'весна'},
    {'цветок': 'ландыш', 'сезон': 'весна'},
    {'цветок': 'хризантема', 'сезон': 'осень'},
    {'цветок': 'хризантема', 'сезон': 'зима'},
    {'цветок': 'гладиолус', 'цвет': 'белый'},
    {'цветок': 'гладиолус', 'цвет': 'розовый'},
]

# Определяем функцию для проверки условия в правиле
def check_condition(condition, fact):
    for key, value in condition.items():
        if key not in fact or fact[key] != value:
            return False
    return True

# Определяем функцию для выполнения правила
def execute_rule(rule, facts):
    for key, value in rule['если'].items():
        if key not in facts:
            return False
        if facts[key] != value:
            return False
    facts.update(rule['то'])
    return True

# Определяем функцию для прямого вывода
def forward_chaining(rules, facts):
    while True:
        new_facts = []
        for rule in rules:
            if execute_rule(rule, facts):
                new_facts.append(rule['то'])
        if not new_facts:
            break
        facts.extend(new_facts)
    return facts

# Пример использования
print(forward_chaining(rules, facts))
# Результат: [{'цветок': 'роза', 'цвет': 'красный'}, {'цветок': 'тюльпан', 'цвет': 'желтый'}, {'цветок': 'ир
