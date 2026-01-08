from collections import deque
class Tree:
    def __init__(self, value):
        self.data = value
        self.children = []

def print_tree_detailed(root):
    if(root==None): # Edge Case
        return
    
    print(f"{root.data}:",end = "")

    for eachChild in root.children:
        print(eachChild.data,end = ",")

    print()

    for eachChild in root.children:
        print_tree_detailed(eachChild)

def take_input_optimized():
    value =int(input("Enter the value for root: "))
    root = Tree(value)

    queue = deque([root])

    while queue: # while queue != None
        current_node= queue.popleft()
        num_children = int(input(f"Enter the number of children for {current_node.data}: "))

        for child in range(num_children):
            value =int(input(f"Enter the value for {current_node.data} child number {child + 1}: "))
            new_node = Tree(value)
            current_node.children.append(new_node)
            queue.append(new_node)
    return root 