if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr1 = list(arr)
    
    new_list = []
    
    for i in range(0, len(arr1)):
        max_value = max(arr1)
        arr1.remove(max_value)
        new_list.append(max_value)
    new_list_set = set(new_list)
    
    final_list = sorted(list(new_list_set))
    
    print(final_list[-2])