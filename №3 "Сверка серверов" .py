server_a = set(input('Введите имена фалов на сервере a: ').split())
server_b = set(input('Введите имена фалов на сервере b: ').split())

common_files = server_a & server_b
print(f'Общие файды: {' '.join(sorted(common_files))}')

lost_files = server_a - server_b
print(f'Потерянные файлы: {' '.join(sorted(lost_files))}')
