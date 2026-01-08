class node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_LL(head):
    temp = head
    while(temp!=None):
        print(temp.data,end="->")
        temp = temp.next

    print()
    return


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
def lengthOfLL(head):
    #temp = head
    ans = 0
    while head != None:
        head = head.next
        ans += 1
    
    return ans

def get_LL_from_List(list):
    if len(list) ==0:
        return None
    new_node = node(list[0])
    head = new_node
    tail = head
    head.next = tail

    for i in range(1,len(list)):
        new_node = node(list[i])
        tail.next = new_node
        tail = new_node
    
    return head


