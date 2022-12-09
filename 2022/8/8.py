def vizir(lines: list[str]) -> int:
    visible = len(lines[0]) * 2 # top and bottom trees
    highestFromTop = [int(x) for x in lines[0][1:-1]]

    for h, line in enumerate(lines[1:-1]):
        visible += 2 #trees at the edges
        line = [int(x) for x in line]
        highestLeft = line[0]
        for i, tree in enumerate(line[1:-1]):
            lt_vis = False
            #from left and top
            if highestLeft < tree:
                lt_vis = True
                highestLeft = tree
            
            if highestFromTop[i] < tree:
                lt_vis = True
                highestFromTop[i] = tree
            
            if lt_vis:
                visible += 1
                continue

            #from right and bottom
            rb_vis = True
            for j in line[i+2:]:
                if j >= tree:
                    rb_vis = False
                    break
            
            if rb_vis:
                visible += 1
                continue
            
            rb_vis = True
            b_lines = [int(x[i+1]) for x in lines[h+2:]]
            print(b_lines)
            for j in b_lines:
                if j >= tree:
                    rb_vis = False
                    break
            
            if rb_vis:
                visible += 1
            

    return visible

with open('data.txt','r') as infile:
    text = infile.read()
    print( vizir(text.splitlines()) )