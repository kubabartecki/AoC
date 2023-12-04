def cards(lines: list[str]) -> int:
    points_sum = 0

    for line in lines:
        count_wins = 0
        nums_left, nums_right = line.split(':')[1].split('|')
        nums = nums_left.split()
        nums_winning = nums_right.split()
        for win in nums_winning:
            if win in nums:
                count_wins += 1
        if count_wins > 0:
            points_sum += 2 ** (count_wins - 1)
    return points_sum
        
with open('input.txt','r') as infile:
    text = infile.read()
    print( cards(text.splitlines()) )