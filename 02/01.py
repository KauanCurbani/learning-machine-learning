

entries = [1,7,5]
weights = [0.8, 0.1,0]

def sum(e, w):
    s = 0
    for i in range(3):
        s += e[i] * w[i]
    return s


s = sum(entries, weights)

def stepFunction(sum):
    if(sum >= 1):
        return 1
    return 0

result = stepFunction(s)

print(result)
