from typing import List

"""
It would be more clear to use p1 and p2 pointers to indicate
the start of each two consecutive char groups. 
"""


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        group_length = 1
        start_group_index = 0
        seq_char = chars[0]

        for next_char in chars[1:]:
            if next_char == seq_char:
                group_length += 1
            else:
                if group_length == 1:
                    seq_char = next_char
                    start_group_index += 1
                    continue
                code = str(group_length)
                for j, digit in enumerate(code):
                    chars[start_group_index + 1 + j] = digit
                del chars[
                    start_group_index + len(code) + 1:start_group_index + group_length]
                start_group_index = start_group_index + 1 + len(code)

                seq_char = next_char
                group_length = 1

        if group_length != 1:
            code = str(group_length)
            for j, digit in enumerate(code):
                chars[start_group_index + 1 + j] = digit
            del chars[
                start_group_index + len(code) + 1:start_group_index + group_length]

        return len(chars)


sol = Solution()
# assert sol.compress(["a", "a", "b", "b", "c", "c", "c"]) == 6
assert sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]) == 4
