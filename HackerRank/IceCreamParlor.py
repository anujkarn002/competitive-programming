#!/bin/python3

# https://www.hackerrank.com/challenges/icecream-parlor/problem

import math
import os
import random
import re
import sys
from itertools import combinations
# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    for comb in combinations(arr, 2):
        if sum(comb) == m:
            a = arr.index(comb[0])+1
            b = arr.index(comb[1])+1 if a != arr.index(comb[1])+1 else arr.index(comb[1], a)+1
            r = [a, b]
            return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

