# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()

n = int(input())

for i in range(n):
    ops = input().split()
    
    if ops[0] == "append":
        d.append(int(ops[1]))
    elif ops[0] == "appendleft":
        d.appendleft(int(ops[1]))
    elif ops[0] == "pop":
        d.pop()
    else:
        d.popleft()
    
for j in d:
    print(j, end=" ")