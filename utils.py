import random

def getOrder(names, excluded, picks):    
    names = random.sample(names, len(names))
    included = [name for name in names if name not in excluded]
    included = random.sample(included, len(included))
    output = included[:picks]
    names = [name for name in names if name not in output]
    output += random.sample(names, len(names))
    return output 

def printOrder(names, excluded, seed=None, picks=1):
    random.seed(seed)
    print("\n\nThe official order is...\n") 
    for i, n in enumerate(getOrder(names, excluded, picks)):
        print(i+1, ")\t", n)

def makeItLookNice(n, arr):
    n += ":\t"
    if len(n) <= 8: n += "\t"
    for i in arr:
        n += str(f'{i:2.2f}').zfill(5) + '%  '
    return n[:-2]

def ordinal(n):
    if 10 <= n % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"

def printSample(names, excluded, n, picks=1):
    import numpy as np
    print("Percentage of the time each player got each draft pick in ", n, " samples")
    header = "Player\t\t  " + "  ".join(f"{ordinal(i+1):<6}" for i in range(len(names)))
    print(header)
    out = np.zeros((len(names), len(names)), dtype="float64")
    for i in range(n):
        order = getOrder(names, excluded, picks)
        for j, name in enumerate(order):
            out[names.index(name)][j] += 1
    arr = np.divide(out, (n/100))
    for i, name in enumerate(names):
        print(makeItLookNice(name, arr[i,:]))
    

