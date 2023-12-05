def location(lines: list[str]) -> int:
    seeds = [int(num) for num in lines[0].split(':')[1].split()]
    visited_seed = [False for x in range(len(seeds))]

    for line in lines[1:]:
        if not line:
            continue
        if ':' in line:
            visited_seed = [False for x in range(len(seeds))]
            continue

        dest_start, source_start, num_range = [int(num) for num in line.split()]
        
        for i in range(len(seeds)):
            if not visited_seed[i]:
                if source_start <= seeds[i] < source_start + num_range:
                    seeds[i] = dest_start + (seeds[i] - source_start)
                    visited_seed[i] = True

    return min(seeds)
        
with open('input.txt','r') as infile:
    text = infile.read()
    print( location(text.splitlines()) )