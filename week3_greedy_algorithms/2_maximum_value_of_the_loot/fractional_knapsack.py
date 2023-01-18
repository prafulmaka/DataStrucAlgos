from sys import stdin

data = list(map(int, input().split()))
print("Data Original: ", data)
n, capacity = data[0:2]
print("Capacity: ", capacity)
values = data[2:(2 * n + 2):2]
print("Values", values)
weights = data[3:(2 * n + 2):2]
print("Weights: ", weights)


# # Original
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
#     data = list(map(int, stdin.read().split()))
#     n, capacity = data[0:2]
#     values = data[2:(2 * n + 2):2]
#     weights = data[3:(2 * n + 2):2]
#     opt_value = optimal_value(capacity, weights, values)
#     print("{:.10f}".format(opt_value))
