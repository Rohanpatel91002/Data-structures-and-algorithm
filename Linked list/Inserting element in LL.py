from Common import node, print_ll, optimized_take_input

head = optimized_take_input()
print_ll(head)
def insert_at_head(head, value):
    new_node = node(value)

    new_node.next = head
    head = new_node
    return head
# print("after inserting at head")
# head1 = insert_at_head(head,100)
# print_ll(head1)

def insert_at_tail(head, value):
    new_node = node(200)
    if head == None:
        return new_node
    temp = head
    while temp.next != None:
        temp = temp.next
    
    temp.next = new_node
    return head

# print("after inserting at tail")
# head2 = insert_at_tail(head1,200)
# print_ll(head2)


def insert_at_tail_recursively(head, value):
    new_node = node(value)
    if head == None:
        return new_node
    if head.next == None:
        head.next = new_node
        return head
    head.next = insert_at_tail_recursively(head.next, value)
    return head



def insert_at_index(head, value, index):

    if index == 0:
        return insert_at_head(head, value)
    new_node = node(value)
    temp = head
    count = 0

    while temp != None and count < index-1:
        count +=1
        temp = temp.next
    
    if temp == None:
        return "Invalid index"
    
    new_node.next = temp.next
    temp.next = new_node

    return head
    
head1 = optimized_take_input()    
print("after inserting at index")
head2 = insert_at_index(head1,35,3)
print_ll(head2)

def insert_node(head, index, data):
    if index == 0: # we are inserting data when at Linked list's head when head points at index
        return insert_at_head(head, data)
    
    head.next = insert_node(head.next, index-1, data)
    return head
    


    
