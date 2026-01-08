from Common import *

def merge_sorted_LL(head1, head2):
    new_head = None
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data <= head2.data:
        new_head = head1
        head1 = head1.next
                
    elif head2.data< head1.data:
        new_head = head2
        head2 = head2.next

    temp = new_head
    while head1 !=None and head2 != None:

        if head1.data <= head2.data:
            temp.next = head1
            head1= head1.next

        elif head2.data< head1.data:
            temp.next = head2
            head2 = head2.next
        temp = temp.next 

    if head1 == None:
        temp.next = head2
    if head2 == None:
        temp.next = head1
    
    return new_head


head1 = get_LL_from_List([1,3,6,7])
head2 = get_LL_from_List([2,4,6,8,9])

print_LL(merge_sorted_LL(head1, head2))