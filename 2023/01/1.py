def calibration_val(lines: list[str]) -> int:
    result = 0 
    for line in lines:
        first_added = False
        for letter in line:
            ascii_letter = ord(letter)
            if ascii_letter >= 48 and ascii_letter <= 57:
                if not first_added:
                    first_num : str = letter
                    first_added = True
                last_num : str = letter
        result += int(first_num + last_num)
    return result

with open('input.txt','r') as infile:
    text = infile.read()
    print( calibration_val(text.splitlines()) )