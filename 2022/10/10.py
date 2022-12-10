def signal(lines: list[str]) -> int:
    strength = 0
    cycle = 0
    x_register = 1
    for line in lines:
        oper = line.split()
        cycle += 1

        if cycle % 40  == 20:
            strength += cycle * x_register

        if oper[0] != "noop":
            cycle += 1
            if cycle % 40 == 20:
                strength += cycle * x_register
            x_register += int(oper[1])
        
        if cycle >= 220:
            break
        
    return strength

with open('data.txt','r') as infile:
    text = infile.read()
    print( signal(text.splitlines()) )