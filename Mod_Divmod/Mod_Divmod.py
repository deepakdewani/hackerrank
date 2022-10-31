# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
m = int(input())

s = divmod(n, m)

print(s[0])
print(s[1])
print(s)
