#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    bird_dict = {}
    for i in set(arr):
        bird_dict[i] = arr.count(i)
        
    max_frequency = max(bird_dict.values())    
    frequent_birds = [i for (i,j) in bird_dict.items() if j == max_frequency ]  
    return sorted(frequent_birds)[0]   


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
