def main():

    T = int(input())
    for test_i in range(1, T+1):
        input()
        dices = list(map(int, input().split()))
        dices.sort()
        seq_size = 0
        for dice in dices:
            if dice > seq_size:
                seq_size += 1

        print(f"Case #{test_i}: {seq_size}")


if __name__ == "__main__":
    main()
