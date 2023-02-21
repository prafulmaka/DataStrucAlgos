def optimal_summands(n):
    summands = []
    # write your code here
    right = n
    left = 1

    while right != 0:
        if left < (right / 2):
            summands.append(left)
            right -= left
        else:
            summands.append(right)
            right = 0
        left += 1

    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
