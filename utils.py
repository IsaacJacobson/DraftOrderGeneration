import random
import numpy as np

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

def printSample(names, excluded, n, picks=1):
    print("Percentage of the time each player got each draft pick in ", n, " samples")
    print("Player\t\t  1st     2nd     3rd     4th     5th     6th     7th     8th     9th     10th    11th    12th")
    out = np.zeros((len(names), len(names)), dtype="float64")
    for i in range(n):
        order = getOrder(names, excluded, picks)
        for j, name in enumerate(order):
            out[names.index(name)][j] += 1
    arr = np.divide(out, (n/100))
    for i, n in enumerate(names):
        print(makeItLookNice(n, arr[i,:]))
    

