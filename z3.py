number_of_rows = dict()
files = ['1.txt', '2.txt', '3.txt']
for file in files:
    with open(file, encoding='UTF-8') as opened_file:
        count_lines = 0
        for line in opened_file:
            count_lines += 1
    number_of_rows[file] = count_lines

number_of_rows = dict(sorted(number_of_rows.items(), key=lambda x: x[1]))

# если файл output.txt уже существует - он будет перезаписан
with open('output.txt', 'w', encoding='UTF-8') as opened_file:
    opened_file.write('')

for file in number_of_rows:
    with open(file, encoding='UTF-8') as origin_file:
        text = origin_file.read()
    rows = number_of_rows[file]
    final_text = f'{file}\n{rows}\n{text}\n'
    with open('output.txt', 'a', encoding='UTF-8') as target_file:
        target_file.write(final_text)
