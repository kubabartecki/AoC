def score(lines: list[str]) -> int:
    points = 0

    for h, line in enumerate(lines[1:-1]):
    
        line = [int(x) for x in line]
        for i, tree in enumerate(line[1:-1]):
            
            l=0
            r=0
            t=0
            b=0
            #to left
            for j in line[i::-1]:
                l += 1
                if j >= tree:
                    break
            #to right
            for j in line[i+2:]:
                r += 1
                if j >= tree:
                    break

            #to top
            
            for j in lines[h::-1]:
                t += 1
                if int(j[i+1]) >= tree:
                    break

            #to bottom
            for j in lines[h+2:]:
                b += 1
                if int(j[i+1]) >= tree:
                    break
   
            current = l * r * t * b
            if current > points:
                points = current
           
    return points

with open('data.txt','r') as infile:
    text = infile.read()
    print( score(text.splitlines()) )