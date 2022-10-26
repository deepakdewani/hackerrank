# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

no_of_shoes = int(input())
size_of_shoes = collections.Counter(map(int, input().split()))
no_of_customer = int(input())
money = 0

for i in range(no_of_customer):
    (size, price) = map(int, input().split())
    
    if size_of_shoes[size] > 0:
        size_of_shoes[size] -= 1
        money += price
        
print(money)