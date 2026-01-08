def merge_sort(nums):

    if len(nums) <= 1:
        return nums
    
    middle= len(nums)//2

    left_half = merge_sort(nums[:middle])
    right_half = merge_sort(nums[middle:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = 0
    j = 0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i+=1
        else:
            sorted_list.append(right[j])
            j+=1
    
    while i<len(left):
        sorted_list.append(left[i])
        i+=1
    
    while j<len(right):
        sorted_list.append(right[j])
        j+=1
    
    return sorted_list

nums = [5, 2, 9, 1, 5, 6, -1, -2]
print(merge_sort(nums))