# Sample Problem

def main():
    T = int(input().split()[0])
    for test_i in range(1, T+1):
        n, m = list(map(int, input().split(' ')))
        c = list(map(int, input().split(' ')))
        total_candies = sum(c)
        result = total_candies % m
        print(f"Case #{test_i}: {result}")


if __name__ == "__main__":
    main()