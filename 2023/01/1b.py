def calibration_val(lines: list[str]) -> int:
    result = 0
    num_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six' : '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for line in lines:
        first_added = False
        num_seq = ""
        for letter in line:
            ascii_letter = ord(letter)
            if ascii_letter >= 48 and ascii_letter <= 57:
                num_seq = ""
                if not first_added:
                    first_num : str = letter
                    first_added = True
                last_num : str = letter
            else:
                num_seq += letter
                num_seq = num_seq[-5:]
                for i in range(3, len(num_seq) + 1):
                    new_word = num_seq[-i:]
                    if new_word in num_dict:
                        letter = num_dict[new_word]
                        if not first_added:
                            first_num : str = letter
                            first_added = True
                        last_num : str = letter
        result += int(first_num + last_num)
    return result

with open('input.txt','r') as infile:
    text = infile.read()
    print( calibration_val(text.splitlines()) )