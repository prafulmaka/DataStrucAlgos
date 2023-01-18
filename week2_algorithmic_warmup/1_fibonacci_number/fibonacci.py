def fibonacci_number(n):
    if n <= 1:
        return n

    else:
        total = [0, 1]
        for x in range(1, n, 1):
            summy = total[-1] + total[-2]
            total.append(summy)

    return total[-1]


if __name__ == '__main__':
    input_n = int(input())
    # input_n = 50
    print(fibonacci_number(input_n))


# # ORIGINAL
# def fibonacci_number(n):
#     if n <= 1:
#         return n
#
#     return fibonacci_number(n - 1) + fibonacci_number(n - 2)
#
#
# if __name__ == '__main__':
#     # input_n = int(input())
#     input_n = 50
#     print(fibonacci_number(input_n))
