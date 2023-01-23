from sys import stdin


def optimal_value(capacity, weights, values):

    def get_ratio(values, weights):



    value = 0
    # write your code here

    # Test: 3 50 60 20 100 50 120 30
    # Test: 2 30 100 20 50 50

    print("Capacity: ", capacity)
    print("Weights: ", weights)
    print("Value: ", values)

    # To find most expensive and index of most expensive
    # print("Max: ", max(values))
    # print("Index: ", values.index(max(values)))

    while (capacity > 0):
        # Set most expensive, index of most expensive
        most_expensive = max(values)
        ix_most_expensive = values.index(max(values))

        # If capacity is less than or equal to the weight of most expensive
        if capacity <= weights[ix_most_expensive]:
            print("True")
            value = value + (capacity * most_expensive)
            capacity = 0
            print(capacity)

        # If capacity is more than the weight of most expensive
        if capacity > weights[ix_most_expensive]:
            print("False")
            value = value + (capacity * most_expensive)
            capacity = capacity - weights[ix_most_expensive]
            values.remove(values[ix_most_expensive])
            weights.remove(weights[ix_most_expensive])
            print(capacity)

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.readline().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

# # # Original
# from sys import stdin
#
#
# def optimal_value(capacity, weights, values):
#     value = 0
#     # write your code here
#
#     return value
#
#
# if __name__ == "__main__":
#     data = list(map(int, stdin.readline().split()))
#     n, capacity = data[0:2]
#     values = data[2:(2 * n + 2):2]
#     weights = data[3:(2 * n + 2):2]
#     opt_value = optimal_value(capacity, weights, values)
#     print("{:.10f}".format(opt_value))
