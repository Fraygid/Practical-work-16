cia = set(input('Введите список имен ЦРУ: ').split())
mi6 = set(input('Введите список имен МИ-6: ').split())
kgb = set(input('Введите список имен КГБ: ').split())

double_agents = (cia & mi6) - kgb

sorted_agents = sorted(double_agents, reverse=True)
if sorted_agents:
    print(' '.join(sorted_agents))
else:
    print('Нету двойных агентов')
