#what do we want to return - Boolean (True, exists) or index or value itself (?)
#return the index 
#What is the space and time complexity of this algorithm 
#O(log n) time complexity

#Gather requirements -
#1. the target is a value in our list, but we are using list indices to calculate where we look



sorted_list = [1,2,4,5,8,9,12,15,75,88,91,95,100]
target = 100
def binary_search(sorted_list, target):
    left_idx = 0
    right_idx = len(sorted_list) -1
    print(right_idx)



    while(left_idx <= right_idx):
        middle_idx = int((left_idx + right_idx) / 2) 

        if(sorted_list[middle_idx] == target):
            return middle_idx
        elif(target < sorted_list[middle_idx]):
            right_idx = middle_idx - 1
        else:
            left_idx = middle_idx + 1
    
    return -1 #if the value isn't in the list, return -1 

result = binary_search(sorted_list, target)
print('the target number is at list index:', result)


