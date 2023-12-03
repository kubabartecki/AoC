def engine(lines: list[str]) -> int:
    part_sum = 0
    nums = [[0 for x in range(len(lines[0]))] for y in range(len(lines))]

    for i in range(len(lines)):
        num = ""
        for j in range(len(lines[0])):
            if lines[i][j].isdecimal():
                num += lines[i][j]
            elif num:
                for k in range(j - len(num), j):
                    nums[i][k] = int(num)
                num = ""
        # if number ends on the last row index
        if num:
            for k in range(len(lines[0]) - len(num), len(lines[0])):
                nums[i][k] = int(num)

    # search for symbols and collect nums around
    dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if not (lines[i][j].isdecimal() or lines[i][j] == '.'):
                part_set = set()
                for dir in dirs:
                    y = i + dir[0]
                    x = j + dir[1]
                    if x >= 0 and y >= 0 and x < len(lines[0]) and y < len(lines):
                        part_set.add(nums[y][x])
                part_sum += sum(part_set)
    return part_sum


with open('input.txt','r') as infile:
    text = infile.read()
    print( engine(text.splitlines()) )