# Queries Minimum Waiting Time (Greedy, Easy)

# Time O(nlog(n)); Space O(1); n is the number of queries
def minimumWaitingTime(queries):
    queries.sort()
    multiplication_factor = len(queries) - 1
    waiting_time = 0
    for query_time in queries:
        waiting_time += query_time * multiplication_factor
        multiplication_factor -= 1

    return waiting_time