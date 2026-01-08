class node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_ll(head):
    if head == None:
        return
    
    print(head.data)
    return print_ll(head.next)

# this is optimized way to get new input for linked list, time complexity is O(n)
def optimized_take_input():
    value = int(input("enter the value of the linked list: "))
    head = None
    tail = None

    while value != -1:
        new_node = node(value)
        if head == None:
            head= new_node
            tail = new_node

        else:
            tail.next = new_node
            tail= new_node
        
        value = int(input("enter the value of the linked list: "))
    
    return head

print_ll(optimized_take_input())