def binarysearch(nums, x, s, e):
    if s>e:
        return False
    
    middle = s + (e-s)//2

    if x == nums[middle]:
        return True
    
    if x>middle:
        return binarysearch(nums, x, middle+1, e)
    
    return binarysearch(nums, x, s, middle-1)


nums = [1,3,5,7,9,11,13,15]

#print(binarysearch(nums, -5, 0, len(nums)-1))
print(5//3)