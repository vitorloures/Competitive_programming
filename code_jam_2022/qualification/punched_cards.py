def main():

    T = int(input().split()[0])
    for test_i in range(1, T+1):
        R, C = map(int, input().split())
        rows = []
        for row in range(2*R+1):
            row_string_builder = []
            for col in range(2*C+1):
                if row < 2 and col < 2:
                    row_string_builder.append('.')
                elif row % 2 == 0:
                    if col % 2 == 0:
                        row_string_builder.append('+')
                    else:
                        row_string_builder.append('-')
                elif row % 2 == 1:
                    if col % 2 == 0:
                        row_string_builder.append('|')
                    else:
                        row_string_builder.append('.')
            row_string_builder.append('\n')
            rows.append("".join(row_string_builder))

        output = "".join(rows)
        print(f"Case #{test_i}: \n{output}")


if __name__ == "__main__":
    main()
