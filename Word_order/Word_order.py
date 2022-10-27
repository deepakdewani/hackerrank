# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter, OrderedDict

n = int(input())

d = OrderedDict()

for i in range(n):
    word = input()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
    
print(len(d))

for k, v in d.items():
    print(v, end = " ")