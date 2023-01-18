def lcm(a, b):
    product = a * b

    while b != 0:
        remainder = a % b
        a = b
        b = remainder


    return int(product/a)

    assert False


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))


# # Original
# def lcm(a, b):
#     for l in range(1, a * b + 1):
#         if l % a == 0 and l % b == 0:
#             return l
#
#     assert False
#
#
# if __name__ == '__main__':
#     a, b = map(int, input().split())
#     print(lcm(a, b))

