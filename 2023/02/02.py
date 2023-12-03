def gamez(lines: list[str]) -> int:
    id_sum = 0
    color_cred = {'red': 12, 'green': 13, 'blue': 14}
    for line in lines:
        color_count = {'red': 0, 'green': 0, 'blue': 0}
        subsets = line.split(';')
        id = subsets[0].split()[1].strip(':')
        # deleting game label
        subsets[0] = subsets[0].split(':')[1]
        for subset in subsets:
            colors = subset.split(',')
            for color in colors:
                num, col = color.split()
                color_count[col] = max(color_count[col], int(num))
        
        add = True
        for color in color_cred:
            if color_cred[color] < color_count[color]:
                add = False
        if add: id_sum += int(id)
    return id_sum

def gamez_one(lines: list[str]) -> int:
    return sum([0 if False in [False for num_color in [subset.split() for subset in subsets.split(',')] if num_color[1] == 'red' and int(num_color[0]) > 12 or num_color[1] == 'green' and int(num_color[0]) > 13 or num_color[1] == 'blue' and int(num_color[0]) > 14] else int(id) for id, subsets in [(line.split()[1].replace(':', ''), line.split(':')[1].replace(';', ',')) for line in lines]])

with open('input.txt','r') as infile:
    text = infile.read()
    print( gamez_one(text.splitlines()) )