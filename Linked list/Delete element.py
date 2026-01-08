from Common import node, print_ll, optimized_take_input
head = optimized_take_input()
print_ll(head)
def delete_at_head(head):
    if head == None or head.next == None:
        return None
    head = head.next

    return head

def delete_at_tail(head):
    temp = head
    if temp == None or temp.next == None:
        return None
    
    while temp.next.next != None:
        temp = temp.next

    temp.next = None
    return head

def delete_at_tail_recursively(head):
    if head.next == None or head==None:
        return None
    head.next = delete_at_tail_recursively(head.next)

    return head
# head = delete_at_tail_recursively(head)
# print("after deliting tail node")
# print_ll(head)

def delete_at_index(head, index):
    if head == None or head.next == None:
        return None
    
    temp = head
    count = 0
    while count< index -1:
        temp = temp.next
        count+=1
    temp.next = temp.next.next

    return head

# head = delete_at_index(head,2)
# print("after deliting tail node at index")
# print_ll(head)

def delete_at_value(head,value):
    if head == None:
        return None
    temp = head

    while temp.next.data != value:
        temp = temp.next

    if temp.next.next == None:
        temp.next == None
    else:
        temp.next = temp.next.next
    
    return head

# head = delete_at_value(head,30)
# print("after deliting tail node at value")
# print_ll(head)

def delete_at_index_recursively(head, index):
    if index ==0:
        return delete_at_head(head)
    
    head.next = delete_at_index_recursively(head.next, index-1)
    
    return head

head = delete_at_index_recursively(head,3)
print("after deliting tail node at index recursively")
print_ll(head)
