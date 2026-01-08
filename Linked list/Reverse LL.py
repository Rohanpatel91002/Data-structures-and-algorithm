from Common import *

def reverse_ll_using_recursion(head):

    if head == None or head.next==None:
        return head
    
    small_reverse_LL = reverse_ll_using_recursion(head.next)

    tail_of_recursive_LL = head.next
    tail_of_recursive_LL.next = head
    head.next = None

    return small_reverse_LL

# print_LL(get_LL_from_List([1,2,3,4,5]))

# print_LL(reverse_ll_using_recursion(get_LL_from_List([1,2,3,4,5])))


def reverse_ll_using_iteration(head):
    if head == None or head.next==None:
        return head

    current = head
    prev = None

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    
    return prev

print_LL(get_LL_from_List([1,2,3,4,5]))

print_LL(reverse_ll_using_iteration(get_LL_from_List([1,2,3,4,5])))
