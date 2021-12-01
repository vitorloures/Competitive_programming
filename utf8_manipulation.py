"""
This is my first implementation of utf-8 validation LC problem:
https://leetcode.com/problems/utf-8-validation/solution/
"""

from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # TODO: Fix
        #  O(n): Go through the list once without finishing the execution
        binary_data = self.transformInteger2Binary(data)
        # TODO: Avoid while loops
        # O(n)
        # 2 * n execution time
        # It could be done in n
        while len(binary_data) > 0:
            # cur_byte, cur_character would be a better name
            next_byte = binary_data[0]
            # size_seq could be named n_bytes
            is_valid, size_seq = self.isNBytesSeq(next_byte)

            if not is_valid:
                return False

            if len(binary_data) < size_seq:
                return False
            else:
                seq2analyse = binary_data[:size_seq]
                binary_data = binary_data[size_seq:]

            if size_seq > 1:
                is_valid = self.check_10_presence(size_seq, seq2analyse)
                if not is_valid:
                    return False
        return True

    def check_10_presence(self, size_seq: int, seq2analyse: List) -> bool:
        for byte_pos in range(1, size_seq):
            if seq2analyse[byte_pos][:2] != '10':
                return False
        return True

    def isNBytesSeq(self, next_byte: str) -> tuple:
        if next_byte[0] == '0':
            return True, 1
        elif next_byte[:3] == '110':
            return True, 2
        elif next_byte[:4] == '1110':
            return True, 3
        elif next_byte[:5] == '11110':
            return True, 4
        else:
            return False, -1

    def transformInteger2Binary(self, data: List[int]) -> List[str]:
        binary_list = []
        for i in data:
            binary_i = self.getBinaryString(i)
            binary_list.append(binary_i)
        return binary_list

    # Python provides bin() native function for this
    def getBinaryString(self, integer: int) -> str:
        binary_format = ''
        integer_to_transform = integer % 256

        power_two_seq = [128, 64, 32, 16, 8, 4, 2, 1]
        for power_two_evaluated in power_two_seq:
            if integer_to_transform >= power_two_evaluated:
                binary_format = binary_format + '1'
                integer_to_transform -= power_two_evaluated
            else:
                binary_format += '0'

        return binary_format


sol = Solution()
assert sol.validUtf8([197, 130, 1]) == True
assert sol.validUtf8([235, 140, 4]) == False
print('Test cases passed')