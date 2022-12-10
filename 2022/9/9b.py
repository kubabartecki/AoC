def visited2(lines: list[str]) -> int:
    directions = {"D": [0,-1], "U": [0,1], "R": [1,0], "L":[-1,0]}
    moves = {0: 0, 1:1, -1: -1, 2: 1, -2: -1}

    Thistory = set()
    knotsArray = [[0,0] for x in range(10)] #list of positoins

    for line in lines:
        d, steps = line.split()
        d = directions[d]
        steps = int(steps)
 
        for x in range(steps):
            knotsArray[0][0] += d[0] #head positon update
            knotsArray[0][1] += d[1]

            for k in range(1, 10):
            
                print("knot: ",k, knotsArray[k])
                if abs(knotsArray[k-1][0] - knotsArray[k][0]) > 1 or abs(knotsArray[k-1][1] - knotsArray[k][1]) > 1:
                    print(k, knotsArray[k-1] , knotsArray[k])
                    knotsArray[k][0] += moves[knotsArray[k-1][0] - knotsArray[k][0]]
                    knotsArray[k][1] += moves[knotsArray[k-1][1] - knotsArray[k][1]]
                    print(k, knotsArray[k-1] , knotsArray[k])
                else:
                    break

            #places visited in set of tuples
            Thistory.add((knotsArray[9][0], knotsArray[9][1]))
            
    return len(Thistory)

with open('data.txt','r') as infile:
    text = infile.read()
    print( visited2(text.splitlines()) )