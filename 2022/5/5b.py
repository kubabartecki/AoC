elements = []

with open('data.txt','r') as infile:
    for lines in infile:
        if lines[0] == " ": #end of input
            break
        elements.append(lines[1::4])#list of strings "W L THVFH" - form

    stacks = [ [] for x in range(len(elements[0])) ] #initialize stack
    for line in elements[::-1]:
        for i, elem in enumerate(line):
            stacks[i].append(elem)

    #clean empty elements
    for num in range(len(stacks)):
        while (stacks[num].count(' ')):
            stacks[num].remove(' ')
        
    #print(stacks)

    line = infile.readline()#just skip '\n'
    
    #operations
    for line in infile:
        #get digits from line
        operation = [int(a) for a in line.strip('\n').split(' ') if a.isdigit()]

        for num in reversed(range(operation[0])):
            #operation on stacks
            #pop from (- number of elements to pop) to the top of stack
            stacks[operation[2]-1].append(stacks[operation[1]-1].pop(- num - 1))
    
    result = ""
    for stack in stacks:
        result += str(stack[-1])
        print(stack)
    print(result)