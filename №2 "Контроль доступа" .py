base_id = set(input('Введите базу разрешенных id: ').split())

incoming_id = input('Введите входящие id: ').split()

for i in incoming_id:
    if i in base_id:
        print('OK')
    else:
        print('ADDED')
        base_id.add(i)
