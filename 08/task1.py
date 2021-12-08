with open("sample", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    outputs = [line.split("|")[1].split() for line in lines]

    print(sum([len([code for code in output if len(code) in [2, 3, 4, 7]]) for output in outputs]))
