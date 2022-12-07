#size of all folders
def size(lines: list[str]) -> int:
    size = 0

    for line in lines:
        if line[0].isdigit():          #files
            size += int(line.split()[0])

    return size

def size2Remove(size : int, lines: list[str]) -> int:
    space = 30000000
    toRemove = space - (70000000 - size)
    if toRemove <= 0:
        return 0

    stack = [0]
    current = size
    for line in lines:
        if line[:7] == "$ cd ..":
            tmp = stack.pop()
            stack[-1] += tmp

            if tmp >= toRemove and tmp < current:
                current = tmp

        elif line[:4] == "$ ls":
            stack.append(0)

        elif line[0].isdigit():          #files
            stack[-1] += int(line.split()[0])

    return current

with open('data.txt','r') as infile:
    text = infile.read()
print(size(text.splitlines()))
print(size2Remove( size(text.splitlines()) , text.splitlines()))

