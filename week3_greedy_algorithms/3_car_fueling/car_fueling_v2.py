from sys import stdin

# Test: 500 200 4 100 200 300 400
# Test: 700 200 4 100 200 300 400
# Test: 950 400 4 200 375 550 750
# Test: 1000 300 6 100 400 700 800 900 1000
# Test 100 20 8 0 10 30 40 50 70 90 100

def min_refills(distance, tank, stops):
    # write your code here
    fulltank = tank
    stopcount = 0
    laststop = 0

    if laststop + tank >= distance:
        return 0

    if (len(stops) == 0) | (stops[0] - laststop > tank):
        return -1

    while len(stops) >= 1:
        if ((stops[0] - laststop > tank)):
            return -1

        if (len(stops) == 1) and ((stops[0] + fulltank) < distance):
            return -1

        if (len(stops) == 1) and ((stops[0] == distance)):
            stops = []

        elif len(stops) > 1:
            if ((stops[0] - laststop) <= tank) and ((stops[1] - laststop) <= tank):
                tank -= stops[0] - laststop
                laststop = stops[0]
                stops = stops[1:]

            elif ((stops[0] - laststop) <= tank) | ((stops[1] - laststop) >= tank):
                tank -= stops[0] - laststop
                laststop = stops[0]
                stopcount += 1
                tank = fulltank
                stops = stops[1:]

        elif len(stops) == 1:
            if ((stops[0] - laststop) < tank) and ((distance - laststop) < tank):
                tank -= stops[0] - laststop
                laststop = stops[0]
                stops = []

            else:
                tank -= stops[0] - laststop
                laststop = stops[0]
                stopcount += 1
                tank = fulltank
                stops = []

    return stopcount

if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.readline().split())
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
