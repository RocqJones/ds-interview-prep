import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    my_list = []
    count_pair = 0
    for i in range(n):
        if ar[i] not in my_list:
            my_list.append(ar[i])

        else:
            my_list.remove(ar[i])
            count_pair += 1

    # return count_pair
    print(count_pair)

if __name__ == '__main__':
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    sockMerchant(n, ar)
    # result = sockMerchant(n, ar)

"""
Sample input
9
10 20 20 10 10 30 50 10 20
Sample output
3
"""