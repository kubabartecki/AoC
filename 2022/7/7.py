def size1(lines: list[str]) -> int:
    overal = 0
    limit = 100000
    stack = [0]

    for line in lines:
        if line[:7] == "$ cd ..":
            tmp = stack.pop()
            stack[-1] += tmp
            if tmp <= limit:
                overal += tmp

        elif line[:4] == "$ ls":
            stack.append(0)

        elif line[0].isdigit():          #files
            stack[-1] += int(line.split()[0])
    
    # at the end we need to clear stack
    for i in reversed(range(1, len(stack))):
        if stack[i] <= limit:
            overal += stack[i]
            stack[i-1] += stack[i]
        else:
            break
        
    return overal

with open('data.txt','r') as infile:
    text = infile.read()

print(size1(text.splitlines()))

