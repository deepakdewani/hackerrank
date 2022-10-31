# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
ns = set(map(int, input().split()))

b = int(input())
bs = set(map(int, input().split()))

final_set = ns.intersection(bs)

print(len(final_set))
