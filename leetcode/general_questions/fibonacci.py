# O(n) Time; O(1) Space

def getNthFib(n):
    # Write your code here.
    if n == 1:
        return 0
    if n == 2:
        return 1
    an_2 = 0
    an_1 = 1
    for i in range(3, n+1):
        a_n = an_1 + an_2
        an_2 = an_1
        an_1 = a_n
    return a_n
