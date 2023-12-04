def cards(lines: list[str]) -> int:
    cards_sum = 0
    card_count = [1 for x in range(len(lines))]

    for index, line in enumerate(lines):
        cards_sum += card_count[index]
        count_wins = 0
        nums_left, nums_right = line.split(':')[1].split('|')
        nums = nums_left.split()
        nums_winning = nums_right.split()
        for win in nums_winning:
            if win in nums:
                count_wins += 1
        for w in range(1, count_wins + 1):
            if index + w < len(lines):
                card_count[index + w] += 1 * card_count[index]
            else: break
    return cards_sum
        
with open('input.txt','r') as infile:
    text = infile.read()
    print( cards(text.splitlines()) )