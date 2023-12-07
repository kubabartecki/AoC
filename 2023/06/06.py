def boat(lines: list[str]) -> int:
    # if the input was larger then we could start counting from the middle
    times = lines[0].split(':')[1].split()
    distances = lines[1].split(':')[1].split()

    result = 1
    for time, distance in zip(times, distances):
        ways = 0
        for j in range(int(time)):
            new_distance = j * (int(time) - j)
            if new_distance > int(distance):
                ways += 1
        result *= ways
    return result
        
with open('input.txt','r') as infile:
    text = infile.read()
    print( boat(text.splitlines()) )