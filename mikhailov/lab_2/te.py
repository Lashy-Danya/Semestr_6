# База знаний для цветковых растений
# knowledge_base = [
#     {"plant": "Роза", "color": "Красный", "leaves": "Шипы", "height": "Средний", "type": "Кустарник"},
#     {"plant": "Хризантема", "color": "Желтый", "leaves": "Простые", "height": "Высокий", "type": "Многолетник"},
#     {"plant": "Тюльпан", "color": "Красный", "leaves": "Простые", "height": "Низкий", "type": "Луковичное растение"},
#     {"plant": "Астра", "color": "Фиолетовый", "leaves": "Простые", "height": "Высокий", "type": "Многолетник"},
#     {"plant": "Лилия", "color": "Белый", "leaves": "Простые", "height": "Высокий", "type": "Луковичное растение"}
# ]

# # Функция для поиска типа растения на основе его характеристик
# def find_plant_type(color, leaves, height):
#     for knowledge in knowledge_base:
#         if knowledge["color"] == color and knowledge["leaves"] == leaves and knowledge["height"] == height:
#             return knowledge["type"]
#     return "Не удалось определить тип растения"

# # Пример использования функции
# plant_type = find_plant_type("Красный", "Простые", "Низкий")
# print(plant_type) # "Луковичное растение"

# -------------------------------

# def is_flowering_plant(name, has_petals, has_sepals):
#     """
#     Функция, определяющая, является ли растение цветком на основе его имени, наличия лепестков и чашелистика.
#     """
#     if name in ["Роза", "Тюльпан", "Лилия"]:
#         if has_petals and has_sepals:
#             return True
#     elif name in ["Огуречник", "Подсолнечник", "Пшеница"]:
#         if not has_petals and has_sepals:
#             return True
#     elif name in ["Молодильное яблоко", "Лаванда", "Мятная ива"]:
#         if has_petals and not has_sepals:
#             return True
#     return False


# def get_flower_type(name, has_petals, has_sepals):
#     """
#     Функция, определяющая тип цветка на основе его имени, наличия лепестков и чашелистика.
#     """
#     if is_flowering_plant(name, has_petals, has_sepals):
#         if has_petals and has_sepals:
#             return "Двурядные"
#         elif not has_petals and has_sepals:
#             return "Однорядные"
#         elif has_petals and not has_sepals:
#             return "Бесчашечные"
#     else:
#         return "Растение не является цветком"

# print(get_flower_type("Тюльпан", True, True))
# # 'Двурядные'
# print(get_flower_type("Пшеница", False, True))
# # 'Однорядные'
# print(get_flower_type("Лаванда", True, False))
# # 'Бесчашечные'
# print(get_flower_type("Клубника", True, True))
# # 'Растение не является цветком'

# -------------------------------------------------------

# База знаний
# knowledge_base = [
#     {"name": "Роза", "leaves": "Одиночные", "petals": "Многочисленные", "color": "Разнообразный"},
#     {"name": "Лилия", "leaves": "Одиночные", "petals": "Многочисленные", "color": "Белый"},
#     {"name": "Ирис", "leaves": "Парные", "petals": "Три", "color": "Фиолетовый"},
#     {"name": "Тюльпан", "leaves": "Одиночные", "petals": "Многочисленные", "color": "Красный"},
#     {"name": "Хризантема", "leaves": "Парные", "petals": "Многочисленные", "color": "Разнообразный"}
# ]

# # Правила
# rules = [
#     {"if": "leaves == 'Одиночные' and petals == 'Многочисленные' and color == 'Разнообразный'", "then": "name = 'Роза'"},
#     {"if": "leaves == 'Одиночные' and petals == 'Многочисленные' and color == 'Белый'", "then": "name = 'Лилия'"},
#     {"if": "leaves == 'Парные' and petals == 'Три' and color == 'Фиолетовый'", "then": "name = 'Ирис'"},
#     {"if": "leaves == 'Одиночные' and petals == 'Многочисленные' and color == 'Красный'", "then": "name = 'Тюльпан'"},
#     {"if": "leaves == 'Парные' and petals == 'Многочисленные' and color == 'Разнообразный'", "then": "name = 'Хризантема'"}
# ]

# # Запрос
# query = {"leaves": "Одиночные", "petals": "Многочисленные", "color": "Разнообразный"}

# # Выполнение продукционной системы
# for rule in rules:
#     if eval(rule["if"], query):
#         exec(rule["then"], query)
#         break

# print("Тип растения:", query["name"])

# ---------------------------------------------------

# Факты
# fact_db = [
#     {'name': 'Маргаритка', 'color': 'белый', 'season': 'весна'},
#     {'name': 'Роза', 'color': 'красный', 'season': 'лето'},
#     {'name': 'Тюльпан', 'color': 'красный', 'season': 'весна'},
#     {'name': 'Лилия', 'color': 'белый', 'season': 'лето'}
# ]

# # Правила
# rules = [
#     {'condition': lambda f: f['color'] == 'белый' and f['season'] == 'весна',
#      'action': lambda f: print(f"Растение {f['name']} - это белая весенняя цветущая растение")},
#     {'condition': lambda f: f['color'] == 'красный' and f['season'] == 'лето',
#      'action': lambda f: print(f"Растение {f['name']} - это красное летнее цветущая растение")},
#     {'condition': lambda f: f['color'] == 'красный' and f['season'] == 'весна',
#      'action': lambda f: print(f"Растение {f['name']} - это красное весенняя цветущая растение")},
#     {'condition': lambda f: f['color'] == 'белый' and f['season'] == 'лето',
#      'action': lambda f: print(f"Растение {f['name']} - это белое летнее цветущая растение")}
# ]

# # Продукционная система
# def production_system(fact_db, rules):
#     for fact in fact_db:
#         for rule in rules:
#             if rule['condition'](fact):
#                 rule['action'](fact)
#                 break

# # Пример использования
# production_system(fact_db, rules)

# ----------------------------------------

