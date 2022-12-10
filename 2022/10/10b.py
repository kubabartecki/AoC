def render(lines: list[str]) -> None:
    cycle = 0
    x_register = 1 ###
    render = ""
    for line in lines:
        oper = line.split()

        if cycle%40 >= x_register - 1 and cycle%40 <= x_register + 1:
            render += "#"
        else:
            render += "."
        cycle += 1
        
        if cycle % 40 == 0:
            with open('render.txt','a+') as file:
                file.write(render)
                file.write("\n")
            render = ""

        if oper[0] != "noop":
            if cycle%40 >= x_register - 1 and cycle%40 <= x_register + 1:
                render += "#"
            else:
                render += "."
            cycle += 1

            if cycle % 40 == 0:
                with open('render.txt','a+') as file:
                    file.write(render)
                    file.write("\n")
                render = ""

            x_register += int(oper[1])

with open('data.txt','r') as infile:
    text = infile.read()
    render(text.splitlines())