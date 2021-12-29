sorted_list = [1,4,6,9,11,14,15,16,18,25]
target = 14
def binary_search(sorted_list, target):
    left_idx = 0
    right_idx = len(sorted_list - 1)

    while(left_idx<=right_idx):
        middle_idx = (left_idx + right_idx)/2

        if(sorted_list[middle_idx] == target):
            return middle_idx
        elif(target < sorted_list[middle_idx]):
            right_idx = middle_idx - 1
        else:
            left_idx = middle_idx + 1 
    return-1 
result = binary_search(sorted_list, target)
print(result)