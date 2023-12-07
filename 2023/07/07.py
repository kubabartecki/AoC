def poker(lines: list[str]) -> int:
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    cards.reverse()
    card_weight = {card: weight for weight, card in enumerate(cards)}
    type_buckets = [[] for x in range(7)]

    for line in lines:
        hand, bid = line.split()
        card_counter = {}
        for card in hand:
            card_counter[card] = card_counter.get(card, 0) + 1
        
        best_combination = max(card_counter.values())

        type_index = 0
        if best_combination == 5:
            type_index = 6
        elif best_combination == 4:
            type_index = 5
        elif best_combination == 3:
            if 2 in card_counter.values():
                type_index = 4
            else:
                type_index = 3
        elif best_combination == 2:
            if 2 == list(card_counter.values()).count(2):
                type_index = 2
            else:
                type_index = 1
        elif best_combination == 1:
            type_index = 0
            
        type_buckets[type_index].append([hand, bid])

    # sort in each bucket
    for i in range(len(type_buckets)):
        type_buckets[i] = sorted(type_buckets[i], key=lambda hand: [card_weight[card] for card in hand[0]])

    # iterate buckets in the sequence
    total = 0
    index = 0
    for bucket in type_buckets:

        for _, bid in bucket:
            total += (index + 1) * int(bid)
            index += 1
    return total
        
with open('input.txt','r') as infile:
    text = infile.read()
    print( poker(text.splitlines()) )