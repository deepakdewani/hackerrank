def average(array):
    # your code goes here
    array1 = set(array)
    
    average_count = sum(array1) / len(array1)
    
    return average_count
    
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)