sorted_list = [1,2,3,4,5,6,7,8,9,10,11]
target = 2
def binary_search(sorted_list, target):
    right_idx = len(sorted_list) - 1
    left_idx = 0



    while (left_idx <=   right_idx ):
        middle_idx = int((right_idx + left_idx)/2)
        if(sorted_list[middle_idx]==target):
            return middle_idx
        elif(target < sorted_list[middle_idx]):
            right_idx = middle_idx - 1
        else:
            left_idx = middle_idx + 1
    return -1

value = binary_search(sorted_list,target)
print(value)