def main():

    T = int(input().split()[0])
    for test_i in range(1, T+1):
        N = int(input().split()[0])
        comp = 9 - N % 9
        N_str = str(N)
        min_sol = float('inf')

        i = 0
        if comp != 9:
            while i < len(N_str):
                if comp < int(N_str[i]):
                    gen_str = N_str[:i] + str(comp) + N_str[i:]
                    gen_int = int(gen_str)
                    if gen_int < min_sol:
                        min_sol = gen_int
                    break
                i += 1

            gen_int = 10 * N + comp
            if gen_int < min_sol:
                min_sol = gen_int

        else:
            gen_str = N_str[:1] + '0' + N_str[1:]
            gen_int = int(gen_str)
            if gen_int < min_sol:
                min_sol = gen_int

        print(f"Case #{test_i}: {min_sol}")


if __name__ == "__main__":
    main()