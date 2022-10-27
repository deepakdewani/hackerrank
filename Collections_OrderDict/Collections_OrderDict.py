# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

n = int(input())

d = OrderedDict()

for i in range(n):
    items = input().split()
    item_price = int(items[-1])
    item_name = (" ").join(items[:-1])
    if (d.get(item_name)):
        d[item_name] += item_price
    else:
        d[item_name] = item_price
        
for i in d.keys():
    print(i, d[i])
    