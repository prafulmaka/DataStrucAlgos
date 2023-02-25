from itertools import permutations

# Test 1: 2; 21 2
# Test 2: 3; 23 39 92

def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    numbers.sort(reverse=True)

    largest = []

    while numbers != []:
        max = 0
        for item in numbers:
            if int(str(item) + str(max)) >= int(str(max) + str(item)):
                max = item
        largest.append(max)
        numbers.remove(max)

    largest = int("".join(largest))

    return largest



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
