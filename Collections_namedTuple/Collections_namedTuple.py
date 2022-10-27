# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
headers = list(input().split())
total = 0

for i in range(n):
    total += int(list(input().split())[headers.index("MARKS")])
print(total/ n)
