from typing import Optional


def soundex(name: str) -> str:
    if len(name) < 1:
        raise ValueError

    result = []
    result.append(name[0])

    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'h', 'w']
    chars = name[1:]

    last_char = _number_of_char(name[0].lower())
    for i, char in enumerate(chars):
        char_value = _number_of_char(char)

        if char in ['a', 'e', 'i', 'o', 'u', 'y']:
            last_char = -1
            continue
        elif char in ['h', 'w']:
            continue
        else:
            if char_value == last_char:
                continue

            result.append(str(char_value))
            last_char = char_value

    for vowel in vowels:
        chars.replace(vowel, '')

    while len(result) < 4:
        result.append(str(0))

    return ''.join(result)[:4]


def _number_of_char(char: str) -> Optional[int]:
    from typing import Dict, List

    dic: Dict[int, List[str]] = {
        1: ['b', 'f', 'p', 'v'],
        2: ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z'],
        3: ['d', 't'],
        4: ['l'],
        5: ['m', 'n'],
        6: ['r']
    }

    for key, value in dic.items():
        if char in value:
            return key

    return None
