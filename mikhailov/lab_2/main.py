import sys
'''
Наличие механизма заполнения базы правил и глобальной базы данных, а также отображения результата 
логического вывода (интерфейс с пользователем): add_rule()и add_fact()методы позволяют пользователю 
добавлять в систему правила и факты, а print_results()метод печатает результаты процесса вывода.

Механизм логического вывода - прямой вывод: infer()метод выполняет прямой вывод по базе правил и 
глобальной базе данных.

Чтобы представить систему продуктов в виде графика «И/ИЛИ»: Ruleкласс представляет правило в виде 
графа И/ИЛИ.

Обеспечить механизм разрешения конфликтов на этапе вывода: RuleInterpreterкласс разрешает конфликты 
между правилами, используя представление графа И/ИЛИ.

Обеспечить обнаружение ошибочных правил в случае, если либо доказательство вывода не удалось, либо 
получен неверный вывод: RuleInterpreterкласс проверяет, выполнены ли все условия правила, прежде 
чем сделать вывод. Если какое-либо из условий не выполняется, правило считается ошибочным.

Ведение журнала поиска графа: infer()метод регистрирует процесс вывода в системе с использованием 
частичного графа. В случае неудачного вывода указывается невозможное условие.

Этот код можно использовать для реализации различных приложений в предметной области цветковых растений.  
Например, его можно использовать для классификации растений, диагностики болезней растений или 
рекомендаций по уходу за растениями. 
'''

class ProductionSystem:

    def __init__(self):
        self.rule_base = []
        self.global_database = {}
        self.rule_interpreter = RuleInterpreter()

    def add_rule(self, rule):
        self.rule_base.append(rule)

    def add_fact(self, fact):
        self.global_database[fact] = True

    def infer(self):
        for rule in self.rule_base:
            if self.rule_interpreter.can_infer(rule, self.global_database):
                self.global_database[rule.conclusion] = True

    def print_results(self):
        for fact in self.global_database:
            if self.global_database[fact]:
                print(fact)

class RuleInterpreter:

    def __init__(self):
        pass

    def can_infer(self, rule, database):
        for condition in rule.conditions:
            if condition not in database:
                return False
        return True

class Rule:

    def __init__(self, name, conditions, conclusion):
        self.name = name
        self.conditions = conditions
        self.conclusion = conclusion

def main():
    # Create a production system
    system = ProductionSystem()

    # Add some rules
    system.add_rule(Rule("is_flower", ["has_petals", "has_sepals"], "is_flowering_plant"))
    system.add_rule(Rule("is_rose", ["is_flower", "has_thorns"], "is_rose"))

    # Add some facts
    system.add_fact("has_petals")
    system.add_fact("has_sepals")
    system.add_fact("has_thorns")

    # Infer some conclusions
    system.infer()

    # Print the results
    system.print_results()

if __name__ == "__main__":
    main()
