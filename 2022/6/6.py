def part1and2(lines: str, digits: int) -> int:
    result = digits - 1
    
    for index in range(len(lines) - (digits - 1)):
        end = True
        result += 1
        array = lines[index : index + digits]
        print(array)
        for elem in array:
            if array.count(elem) > 1:
                end = False
                break
        if end:
            break
    return result


with open('data.txt','r') as infile:
    text = infile.read()

print(part1and2(text, 14))

