class node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_ll(head):
    if head == None:
        return
    
    print(head.data)
    return print_ll(head.next)

# this is NOT optimized way to get new input for linked list, time complexity is O(n^2)
def take_input_LL():
    value = int(input("enter the value of the linked list : "))
    head = None

    while value != -1:
        new_node = node(value)
        if head == None:
            head = new_node
        else:
            temp = head
            while temp.next != None:
                temp= temp.next
            temp.next = new_node
        
        value = int(input("enter the value of the linked list : "))
    return head

print_ll(take_input_LL())

