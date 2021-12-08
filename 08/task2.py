def parse_line(line):
    list1, list2 = line.split("|")
    list1 = [''.join(sorted(x)) for x in list1.split()]
    list2 = [''.join(sorted(x)) for x in list2.split()]
    return list1, list2


with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    entries = [parse_line(line) for line in lines]

    count = 0
    for patterns, outputs in entries:
        patterns_len_5 = [p for p in patterns if len(p) == 5]
        patterns_len_6 = [p for p in patterns if len(p) == 6]

        code = dict()
        code[1] = [p for p in patterns if len(p) == 2][0]
        code[7] = [p for p in patterns if len(p) == 3][0]
        code[4] = [p for p in patterns if len(p) == 4][0]
        code[8] = [p for p in patterns if len(p) == 7][0]
        code[3] = [p for p in patterns_len_5 if len(set(code[1]).intersection(p)) == 2][0]
        code[6] = [p for p in patterns_len_6 if len(set(code[1]).intersection(p)) == 1][0]
        code[9] = [p for p in patterns_len_6 if len(set(code[4]).intersection(p)) == 4][0]
        code[5] = [p for p in patterns_len_5 if len(set(code[6]).intersection(p)) == 5][0]
        code[2] = list(set(patterns_len_5).difference({code[3], code[5]}))[0]
        code[0] = list(set(patterns).difference(code.values()))[0]

        mappings = {v: k for k, v in code.items()}
        number = ''.join([str(mappings[output]) for output in outputs])
        count += int(number)

    print(count)
