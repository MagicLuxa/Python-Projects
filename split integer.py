def split_integer(num, parts):
    output = []
    rest = num % parts
    x = (num - rest) / parts
    if rest == 0:
        for i in range(parts):
            output.append(int(x))
    else:
        for i in range(parts - rest):
            output.append(int(x))
        for i in range(rest):
            output.append(int(x + 1))

    return output


print(split_integer(20000000, 35))