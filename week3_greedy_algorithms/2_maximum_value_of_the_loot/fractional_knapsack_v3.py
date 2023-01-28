from sys import stdin

# Test: 3 50 60 20 100 50 120 30
# Test: 2 30 100 20 50 50
# Test: 1 1000 500 30
# Test: 1 10 500 30
# Test 10 1000 100 500 50 50 40 40 30 30 20 20 10 10 70 300 2 2 400 5 600 100

class Item:
    def __init__(self, items):
        self.value = items[0]
        self.weight = items[1]

def get_ratio(values, weights):
    pairs = zip(values, weights)
    ratios = sorted(list(el1 / el2 for el1, el2 in pairs), reverse=True)
    return ratios

def optimal_value(capacity, weights, values):

    value = float(0)

    # Get values and weights as list
    pairs = zip(values, weights)
    items = list((el1, el2) for el1, el2 in pairs)

    # Create Item
    arr = [Item(single_item) for single_item in items]

    # Sort arr
    arr.sort(key=lambda x: (x.value//x.weight), reverse=True)

    for item in arr:
        if item.weight <= capacity:
            capacity -= item.weight
            value += float(float(item.value/item.weight) * item.weight)

        else:
            value += float(float(item.value/item.weight) * capacity)

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.3f}".format(opt_value))


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