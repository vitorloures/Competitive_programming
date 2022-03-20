def main():

    T = int(input().split()[0])
    for test_i in range(1, T+1):
        start, end = map(int, input().split())
        int_numbers = 0
        for value in range(start, end + 1):
            if is_interesting_number(value):
                int_numbers += 1

        print(f"Case #{test_i}: {int_numbers}")


def is_interesting_number(number):
    sum_n = 0
    prod_n = 1
    for dig in str(number):
        sum_n += int(dig)
        prod_n *= int(dig)
    return prod_n % sum_n == 0


if __name__ == "__main__":
    main()
