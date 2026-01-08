class node:
    def __init__(self, data):
        self.data = data
        self.next = None

first  = node(1)
second  = node(2)
third  = node(3)
fourth  = node(4)

first.next = second
second.next = third
third.next = fourth
head = first

def print_ll(head):
    if head == None:
        return
    
    print(head.data)
    return print_ll(head.next)

print_ll(head)

