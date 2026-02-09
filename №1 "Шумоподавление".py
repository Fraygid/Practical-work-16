words = input('Введите строку слов через пробел: ').split()

unique_words = set(words)

print(f'Количество уникальных слов: {len(unique_words)}')

sorted_words = sorted(unique_words)
print(f'Отсортированные по алфавиту слова: {sorted_words}')
