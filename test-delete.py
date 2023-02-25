_ = int(input())
numbers = input().split()

numbers = list(map(str, numbers))

numbers.sort(reverse=True)

largest = int("".join(numbers))
largest_2 = list(map(int, str(largest)))
largest_2.sort(reverse=True)

print("Numbers: ", numbers)
print("Largest: ", largest)
print("Largest_2: ", largest_2)
