def main():

    T = int(input().split()[0])
    for test_i in range(1, T+1):
        N = int(input().split()[0])
        S = str(input().split()[0])
        s = []
        qm_index = []
        is_possible = False
        for i in range(N):
            s.append(S[i])
            if S[i] == "?":
                qm_index.append(i)

        sequence = 0
        for i in range(2**len(qm_index)):
            if len(qm_index) == 0:
                if longestPalindrome("".join(s)) < 5:
                    is_possible = True
                break
            bin_seq = bin(sequence)[2:].zfill(len(qm_index))
            for j, dig in enumerate(bin_seq):
                s[qm_index[j]] = dig
            if longestPalindrome("".join(s)) < 5:
                is_possible = True
                break
            sequence += 1

        if is_possible:
            print(f"Case #{test_i}: POSSIBLE")
        else:
            print(f"Case #{test_i}: IMPOSSIBLE")


def longestPalindrome(s):
    dp = [[False for i in range(len(s))] for i in range(len(s))]
    for i in range(len(s)):
       dp[i][i] = True
    max_length = 1
    start = 0
    for l in range(2,len(s)+1):
        for i in range(len(s)-l+1):
            end = i+l
            if l==2:
                if s[i] == s[end-1]:
                    dp[i][end-1]=True
                    max_length = l
                    start = i
            else:
                if s[i] == s[end-1] and dp[i+1][end-2]:
                    dp[i][end-1]=True
                    max_length = l
                    start = i
    return max_length


if __name__ == "__main__":
    main()
