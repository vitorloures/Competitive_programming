def soundex(word: str) -> str:
    
    first_letter = word[0]
    dict_code = {
        6: ['r'],
        5: ['m', 'n'],
        4: ['l'],
        3: ['d', 't'],
        2: ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z'],
        1: ['b', 'f', 'p', 'v']
        }

    code = first_letter.upper()

    for i in range(1, len(word)):
        letter = word[i]
        for number, consonant_list in dict_code.items():
            if letter in consonant_list:
                if str(number) != code[-1]:
                    code += str(number)
    
    # Assert the minimum length to output
    while len(code) < 4:
        code += '0'

    if len(code) > 4:
        code = code[:4]
    
    return code
