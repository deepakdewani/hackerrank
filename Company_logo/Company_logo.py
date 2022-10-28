import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = sorted(input().strip())
    s1 = Counter(s).most_common(3)
    # s2 = sorted(s1, key = lambda x: (x[1]* -1, x[0]))
    
    for i in range(0, 3):
        print(s1[i][0], s1[i][1])
