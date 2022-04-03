def main():

    T = int(input().split()[0])
    for test_i in range(1, T+1):
        printers = [[0, 0, 0, 0] for i in range(3)]
        for i in range(3):
            printers[i] = list(map(int, input().split()))
        min_inks = printers[0]
        for color in range(4):
            for printer in range(1,3):
                if printers[printer][color] < min_inks[color]:
                    min_inks[color] = printers[printer][color]

        sum_inks = sum(min_inks)
        if sum_inks < 10 ** 6:
            print(f"Case #{test_i}: IMPOSSIBLE")
        else:
            inks_to_extract = sum_inks - 10 ** 6
            color = 0
            while inks_to_extract > 0:
                inks = min_inks[color]
                min_inks[color] = inks - inks_to_extract if inks - inks_to_extract >= 0 else 0
                inks_to_extract = 0 if inks - inks_to_extract >= 0 else inks_to_extract - inks
                color += 1

            print(f"Case #{test_i}: {min_inks[0]} {min_inks[1]} {min_inks[2]} {min_inks[3]}")


if __name__ == "__main__":
    main()
