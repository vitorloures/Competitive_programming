# Valid Subsequence with integer array (Easy)

def isValidSubsequence(array, sequence):
    seq_pos = 0
    for val in array:
        if sequence[seq_pos] == val:
            seq_pos += 1

        if seq_pos == len(sequence):
            return True

    return False