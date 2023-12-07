import math
# just solve 
# -x^2 + xt - d > 0
# where x is time pressed

def boat(lines: list[str]) -> int:
    time = int(lines[0].split(':')[1].replace(" ", ""))
    distance = int(lines[1].split(':')[1].replace(" ", ""))

    delta = time**2 - 4 * -1 * -distance
    s_delta = math.sqrt(delta)
    x1 = math.ceil((-time + s_delta) / -2)
    x2 = math.floor((-time - s_delta) / -2)

    return x2 - x1 + 1
        
with open('input.txt','r') as infile:
    text = infile.read()
    print( boat(text.splitlines()) )