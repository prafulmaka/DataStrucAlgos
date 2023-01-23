values = [60, 100, 120]
weights = [20, 50, 30]

def get_ratio(values, weights):
    pairs = sorted(zip(weights, values), key=lambda t: t[0]/t[1], reverse=True)
    print(pairs)
    test = list(el1 // el2 for el1, el2 in pairs)
    print(test)

get_ratio(weights, values)