def gamez(lines: list[str]) -> int:
    power_sum = 0
    for line in lines:
        color_count = {'red': 0, 'green': 0, 'blue': 0}
        subsets = line.split(';')
        # deleting game label
        subsets[0] = subsets[0].split(':')[1]
        for subset in subsets:
            colors = subset.split(',')
            for color in colors:
                num, col = color.split()
                color_count[col] = max(color_count[col], int(num))
        power = 1
        for c in color_count:
            power *= color_count[c]
        power_sum += power
    return power_sum

with open('input.txt','r') as infile:
    text = infile.read()
    print( gamez(text.splitlines()) )