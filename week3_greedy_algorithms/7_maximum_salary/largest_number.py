from itertools import permutations

def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    numbers.sort(reverse=True)
    largest = int("".join(numbers))

    largest_2 = list(map(str, str(largest)))
    largest_2.sort(reverse=True)
    largest_2 = int("".join(largest_2))

    return largest_2


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))

# # Original
# def largest_number_naive(numbers):
#     numbers = list(map(str, numbers))
#
#     largest = 0
#
#     for permutation in permutations(numbers):
#         largest = max(largest, int("".join(permutation)))
#
#     return largest
#
#
# if __name__ == '__main__':
#     _ = int(input())
#     input_numbers = input().split()
#     print(largest_number_naive(input_numbers))
