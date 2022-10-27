n = int(input())
s = set(map(int, input().split()))

m = int(input())

for i in range(m):
    ops = input().split()
    ops_name = ops[0]
    
    if ops_name == "pop":
        s.pop()
    if ops_name == "remove":
        s.remove(int(ops[1]))
    if ops_name == "discard":
        s.discard(int(ops[1]))
    
print(sum(s))