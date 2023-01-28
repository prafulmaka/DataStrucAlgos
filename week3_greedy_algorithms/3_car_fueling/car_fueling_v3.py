from sys import stdin

# Test: 500 200 4 100 200 300 400
# Test: 700 200 4 100 200 300 400
# Test: 950 400 4 200 375 550 750
# Test: 1000 300 6 100 400 700 800 900 1000


def min_refills(distance, tank, stops):
    # write your code here

    num_refills = 0
    current_position = 0
    current_fuel = tank

    stops = [current_position, *stops, distance]

    while current_position < stops.index(distance):
        current = stops[current_position]
        if (current_fuel < (stops[current_position + 1] - stops[current_position])):
            current_fuel = tank
            num_refills = num_refills + 1

        current_fuel = current_fuel - (stops[current_position + 1] - stops[current_position])

        if current_fuel < 0:
            return -1

        current_position = current_position + 1

    return num_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))

# # Original
# from sys import stdin
#
#
# def min_refills(distance, tank, stops):
#     # write your code here
#     return -1
#
#
# if __name__ == '__main__':
#     d, m, _, *stops = map(int, stdin.read().split())
#     print(min_refills(d, m, stops))
