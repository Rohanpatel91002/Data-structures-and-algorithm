from Common import node, print_ll, optimized_take_input

def lengthOfLL(head):
    #temp = head
    ans = 0
    while head != None:
        temp = temp.next
        ans += 1
    
    return ans
print(lengthOfLL(optimized_take_input()))

def lengthOfLL_recursively(head):

    if head == None:
        return 0
    
    return 1 + lengthOfLL_recursively(head.next)

#print(lengthOfLL_recursively(optimized_take_input()))
