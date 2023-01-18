# Uses python3
# Test
def fibonacci_partial_sum_naive_test(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current
            print("Sum: ", _sum)

        current, _next = _next, current + _next
        print("Current", current)
        print("Next", _next)

    return _sum


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_naive_test(from_, to))



# # Original
# def fibonacci_partial_sum_naive(from_, to):
#     _sum = 0
#
#     current = 0
#     _next  = 1
#
#     for i in range(to + 1):
#         if i >= from_:
#             _sum += current
#
#         current, _next = _next, current + _next
#
#     return _sum % 10
#
#
# if __name__ == '__main__':
#     from_, to = map(int, input().split())
#     print(fibonacci_partial_sum_naive(from_, to))
