# Enter your code here. Read input from STDIN. Print output to STDOUT

m = int(input())
mset = set(map(int, input().split()))
n = int(input())
nset = set(map(int, input().split()))

mdef = mset.difference(nset)
ndef = nset.difference(mset)

output = mdef.union(ndef)

for i in sorted(list(output)):
    print(i)
