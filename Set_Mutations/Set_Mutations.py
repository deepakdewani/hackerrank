# Enter your code here. Read input from STDIN. Print output to STDOUT

A = int(input())
As = set(map(int, input().split()))

N = int(input())

for i in range(N):
    N_ops = input().split()
    N_ops_set = set(map(int, input().split()))
    
    if N_ops[0] == "intersection_update":
        As.intersection_update(N_ops_set)
    elif N_ops[0] == "update":
        As.update(N_ops_set)
    elif N_ops[0] == "symmetric_difference_update":
        As.symmetric_difference_update(N_ops_set)
    else:
        As.difference_update(N_ops_set)
        
print(sum(As))