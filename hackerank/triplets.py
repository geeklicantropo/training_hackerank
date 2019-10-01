import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(3):
        if(a[i] > 100 or b[i] > 100 or a[i] < 1 or b[i] < 1):
            print("Value must be between 1 and 100")
            continue
        elif (a[i] > b[i]):
            alice += 1
        elif (a[i] < b[i]):
            bob += 1
        else:
            alice +=0
            bob +=0
    return (alice, bob)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
