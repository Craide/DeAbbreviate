from random import randint
dict = {}
with open("words.txt", encoding='utf-8') as f:
    for line in f:
        word = line.strip()
        if dict.get(word[0]) is None:
            dict[word[0]] = [word]
        else:
            dict[word[0]].append(word)

abr = 'МИЭТ'.lower()

for j in range(10):
    res = ''
    for i in abr:
        if i == '_':
            continue
        # Выбираем случайное слово из списка
        word = dict[i][randint(0, len(dict[i]) - 1)]
        res += word + ' '
    print(res.strip())