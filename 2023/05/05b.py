def location(lines: list[str]) -> int:
    seeds = [int(num) for num in lines[0].split(':')[1].split()]
    seeds = [[start, seed_range] for start, seed_range in zip(seeds[::2], seeds[1::2])]

    visited_ranges = [False for x in range(len(seeds))]

    for line in lines[1:]:
        if not line:
            continue
        if ':' in line:
            visited_ranges = [False for x in range(len(seeds))]
            continue

        dest_start, source_start, num_range = [int(num) for num in line.split()]
        source_end = source_start + num_range - 1

        for i in range(len(seeds)):
            if not visited_ranges[i]:
                seed_start = seeds[i][0]
                seed_end = seeds[i][0] + seeds[i][1] - 1
            
                new_start = max(seed_start, source_start)
                new_end = min(seed_end, source_end)
                new_range = new_end - new_start + 1
                
                # not in range
                if new_range <= 0:
                    continue
                
                # create subset for common part
                new_dest = dest_start + (new_start - source_start)
                seeds[i] = [new_dest, new_range]
                visited_ranges[i] = True

                # create subset for old left part
                if seed_start < source_start:
                    seeds.append([seed_start, source_start - seed_start])
                    visited_ranges.append(False)

                # create subset for old right part
                if seed_end > source_end:
                    seeds.append([seed_end, seed_end - source_end])
                    visited_ranges.append(False)
    
    min_location = seeds[0][0]
    for x, _ in seeds:
        min_location = min(min_location, x)

    return min_location


with open('input.txt','r') as infile:
    text = infile.read()
    print( location(text.splitlines()) )