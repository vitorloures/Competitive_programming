def main():
    alice_kingdom = {'A': 1, 'E': 2, 'I': 3, 'O': 4, 'U': 5, 'a': 6, 'e': 7, 'i': 8, 'o': 9, 'u': 10}
    no_kingdom = {"y": 1, "Y": 2}

    T = int(input().split()[0])
    for test_i in range(1, T+1):
        k = str(input().split()[0])
        last_word = k[-1]
        if alice_kingdom.get(last_word):
            ruler = "Alice"
        elif no_kingdom.get(last_word):
            ruler = "nobody"
        else:
            ruler = "Bob"
        print(f"Case #{test_i}: {k} is ruled by {ruler}.")


if __name__ == "__main__":
    main()
