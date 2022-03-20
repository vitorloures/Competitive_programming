import heapq


def main():
    T = int(input().split()[0])
    for test_i in range(1, T+1):
        n = int(input().split()[0])
        c = list(map(int, input().split(' ')))
        h = 0
        bigger_h = []
        result = []
        for i in range(n):
            num = c[i]
            if num > h:
                heapq.heappush(bigger_h, num)

            if len(bigger_h) > h:
                h += 1
                while len(bigger_h) > 0 and bigger_h[0] <= h:
                    heapq.heappop(bigger_h)

            result.append(h)

        print(f"Case #{test_i}: {' '.join(str(i) for i in result)}")


if __name__ == "__main__":
    main()
