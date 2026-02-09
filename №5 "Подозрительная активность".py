adress_1 = set(input('Введите IP-адресса 1: ').split())
adress_2 = set(input('Введите IP-адресса 2: ').split())
adress_3 = set(input('Введите IP-адресса 3: ').split())

all_adress = adress_1 | adress_2 | adress_3
in_all_three = adress_1 & adress_2 & adress_3

suspicious = all_adress - in_all_three

print(' '.join(sorted(suspicious)))
