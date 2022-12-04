line = input()
overlap = 0

while line:
    first,second = line.split(",")
    fBeg, fEnd = [int(x)for x in first.split("-")]
    sBeg, sEnd = [int(x)for x in second.split("-")]

    if fBeg <= sBeg:
        if fEnd >= sBeg:
            overlap += 1
    elif sEnd >= fBeg:
        overlap += 1

    line = input()
    
print(overlap)