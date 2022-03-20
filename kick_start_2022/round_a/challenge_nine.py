from collections import Counter


def main():

    T = int(input().split()[0])
    for test_i in range(1, T+1):
        N = int(input().split()[0])
        comp = 9 - N % 9
        N_str = str(N)
        possible_strings = []
        for i in range(len(N_str)+2):
            gen_str = N_str[:i]+str(comp)+N_str[i:]
            possible_strings.append(gen_str)
            if comp == 9 and i > 0:
                gen_str = N_str[:i] + '0' + N_str[i:]
                possible_strings.append(gen_str)

        set_int = set()
        for string in possible_strings:
            set_int.add(int(string))
        sol = min(set_int)
        print(f"Case #{test_i}: {sol}")


if __name__ == "__main__":
    main()