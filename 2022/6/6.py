def part1and2(lines: str, digits: int) -> int:
    for index in range(len(lines) - (digits - 1)):
        end = True
        array = lines[index : index + digits]
        
        for elem in array:
            if array.count(elem) > 1:
                end = False
                break
        if end:
            break
    return index + digits


with open('data.txt','r') as infile:
    text = infile.read()

print(part1and2(text, 14))

