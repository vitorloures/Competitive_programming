from collections import Counter


def main():

    T = int(input().split()[0])
    for test_i in range(1, T+1):
        I = str(input().split()[0])
        P = str(input().split()[0])
        count_i = Counter(I)
        count_p = Counter(P)
        diff = 0
        for word, freq in count_i.items():
            if count_p.get(word, 0) > freq:
                diff += count_p[word] - freq
            elif count_p.get(word, 0) < freq:
                diff = -1
                break

        if diff == -1:
            print(f"Case #{test_i}: IMPOSSIBLE")
        else:
            for word, freq in count_p.items():
                if word not in count_i:
                    diff += freq

            print(f"Case #{test_i}: {diff}")


if __name__ == "__main__":
    main()