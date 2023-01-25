# Original
from sys import stdin

# Test: 3 50 60 20 100 50 120 30
# Test: 2 30 100 20 50 50
# Test: 1 1000 500 30
# Test: 1 10 500 30
# Test 10 1000 100 500 50 50 40 40 30 30 20 20 10 10 70 300 2 2 400 5 600 100

def get_ratio(values, weights):
    pairs = zip(values, weights)
    ratios = list(el1 / el2 for el1, el2 in pairs)
    return ratios

def optimal_value(capacity, weights, values):

    value = float(0)

    ratios = get_ratio(values, weights)

    if (capacity == 0) | (len(weights) == 0):
        return 0

    while (capacity > 0) & (len(ratios) > 0):

        most_expensive = max(ratios)
        ix_most_expensive = ratios.index(most_expensive)

        amount = min(weights[ix_most_expensive], capacity)

        value = float(value + (amount * most_expensive))

        capacity = capacity - amount

        ratios.remove(ratios[ix_most_expensive])
        weights.remove(weights[ix_most_expensive])
        values.remove(values[ix_most_expensive])

    return value + optimal_value(capacity, weights, values)


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))


# # Original
# from sys import stdin
#
#
# def optimal_value(capacity, weights, values):
#     value = 0.
#     # write your code here
#
#     return value
#
#
# if __name__ == "__main__":
#     data = list(map(int, stdin.read().split()))
#     n, capacity = data[0:2]
#     values = data[2:(2 * n + 2):2]
#     weights = data[3:(2 * n + 2):2]
#     opt_value = optimal_value(capacity, weights, values)
#     print("{:.10f}".format(opt_value))