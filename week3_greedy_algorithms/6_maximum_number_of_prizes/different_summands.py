def optimal_summands(n):
    summands = []
    # write your code here
    n_original = n

    i = 1

    while (i+1 <= n-1):
        summands.append(i)
        n = n - i
        i = i + 1

    if 0 < n:
        summands.append(n)

    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
