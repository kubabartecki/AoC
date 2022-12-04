line = input()
contain = 0

while line:
    first,second = line.split(",")
    fBeg, fEnd = [int(x) for x in first.split("-")]
    sBeg, sEnd = [int(x) for x in second.split("-")]
    
    if (fBeg <= sBeg) and (fEnd >= sEnd):
        contain += 1
    elif (sBeg <= fBeg) and (sEnd >= fEnd):
        contain += 1
    print(contain)
    line = input()
    
print(contain)