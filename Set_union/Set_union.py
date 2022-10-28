# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
ne = set(map(int, input().split()))

m = int(input())
mf = set(map(int, input().split()))

final_set = ne.union(mf)

print(len(final_set))
