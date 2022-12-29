import sys
import os


def app_table(sin_wor, tab_, character):
    for w in sin_wor:
        chars = [x for x in w]
        is_digit = 0
        for i in chars:
            if not (i in [character.lower(), character] or i.isdigit()):
                is_digit = 1
                break
        if is_digit != 1 and (character.lower() in w or character in w):
            tab_.append(w)


def app_num_table(sin_wor, tab_):
    for w in sin_wor:
        if w.isdigit():
            tab_.append(w)
        elif w.replace('.', '', 1).isdigit() and w.count('.') < 2:
            tab_.append(w)


def function(lines, count, table_q, table_d, table_e, table_da, table):
    for line in lines:
        count += 1
        single_words = line.split()
        app_table(single_words, table_d, "D")
        app_table(single_words, table_e, "E")
        app_table(single_words, table_q, "Q")
        app_table(single_words, table_da, "^")
        app_num_table(single_words, table)


def calc(table, letter, fl):
    res = 0.0
    for val in table:
        val = val.lower()
        first_second = val.split(letter, 1)
        if fl == 2:
            if first_second[0].isnumeric() and first_second[1].isnumeric:
                res += float(first_second[0]) ** float(first_second[1])

        elif fl == 3:
            res += float(first_second[0]) ** float(first_second[1])
    return res


def main_word_counter(file, table_q, table_e, table_d, table_da, table, fl, t_char=None, t_lin=None, t_wor=None):
    result = 0
    filename = file
    file_stat = os.stat(filename)
    size = file_stat.st_size
    with open(filename) as infile:
        lines = 0
        words = 0
        characters = 0
        for line in infile:
            wordslist = line.split()
            lines = lines + 1
            words = words + len(wordslist)
            characters += sum(len(word) for word in wordslist)

    for val in table:
        if fl == 2:
            if val.isnumeric():
                result += int(val)
        elif fl == 3:
            result += float(val)

    result += calc(table_e, "e", flag)
    result += calc(table_d, "d", flag)
    result += calc(table_q, "q", flag)
    result += calc(table_da, "^", flag)

    if flag == 1:
        print(lines, words, characters, size, result)
    elif flag == 2:
        print(lines, words, characters, size, result)
    elif flag == 3:
        print(lines, words, characters, size, result)
    return lines, words, characters, size, result


flag = 0
i = 0
sys.argv = sys.argv[1:]

for value in sys.argv:
    if os.path.isfile('./' + value):
        i = i
    else:
        i += 1

options = sys.argv[:i]
arg = sys.argv[i:]

if i == 0:
    flag = 1

for x in options:
    if x == '-i':
        flag = 2
        break
    elif x == '-d':
        flag = 3
        break

t_lines, t_words, t_chars, t_val, t_size = 0, 0, 0, 0, 0
counter = 0

for name in arg:
    file1 = open(name, 'r')
    for counter, line in enumerate(file1):
        pass
    file1 = open(name, 'r')
    lines_m = file1.readlines()
    value = 0
    tab_q, tab_e, tab_d, tab_da, tab = [], [], [], [], []
    function(lines_m, counter, tab_q, tab_d, tab_e, tab_da, tab)
    x, y, z, w, r, = main_word_counter(name, tab_q, tab_e, tab_d, tab_da, tab, flag)
    t_lines += x
    t_words += y
    t_chars += z
    t_val += r
    t_size += w

print(t_lines, t_words, t_chars, t_size, t_val)
