from Common import *

def middle_of_LL(head):
    middle = lengthOfLL(head) // 2
    count = 0
    temp = head
    while count<middle:
        temp = temp.next
        count+=1
    return temp.data
odd_head = get_LL_from_List([1,2,3,4,5])
even_head = get_LL_from_List([1,2,3,4,5,6])

# print_ll(odd_head)
# print(middle_of_LL(odd_head))

# print_LL(even_head)
# print(middle_of_LL(even_head))

def middle_of_LL_with_pointers(head):

    pointer1 = head
    pointer2 = head

    while pointer2.next != None and pointer2.next.next != None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next.next
    
    return pointer1.data

odd_head = get_LL_from_List([1,2,3,4,5])
even_head = get_LL_from_List([1,2,3,4,5,6,7,8])

print(middle_of_LL_with_pointers(odd_head))
print(middle_of_LL_with_pointers(even_head))