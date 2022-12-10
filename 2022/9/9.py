def visited(lines: list[str]) -> int:
    directions = {"D": [0,-1], "U": [0,1], "R": [1,0], "L":[-1,0]}
    moves = {2: 1, -2: -1}
    Tposition = [0,0]
    Hposition = [0,0]
    Thistory = set()
    for line in lines:
        d, steps = line.split()
        d = directions[d]
        steps = int(steps)
 
        for x in range(steps):
            Hposition[0] += d[0]
            Hposition[1] += d[1]

            if abs(Hposition[0] - Tposition[0]) > 1:
                Tposition[0] += moves[Hposition[0] - Tposition[0]]
                Tposition[1] = Hposition[1]
            elif abs(Hposition[1] - Tposition[1]) > 1:
                Tposition[1] += moves[Hposition[1] - Tposition[1]]
                Tposition[0] = Hposition[0]

            #places visited in set of tuples
            Thistory.add((Tposition[0], Tposition[1]))
            
    return len(Thistory)

with open('data.txt','r') as infile:
    text = infile.read()
    print( visited(text.splitlines()) )