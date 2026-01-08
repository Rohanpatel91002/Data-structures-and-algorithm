from common import *
from collections import deque

def take_input():
    value =int(input("Enter the value for node: "))
    new_node = Tree(value)

    num_children = int(input(f"Enter the number of children for {value}: "))

    for _ in range(num_children):
        child = take_input()
        new_node.children.append(child)
    
    return new_node

# root = take_input()
# print_tree_detailed(root)

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

root = take_input_optimized()
print_tree_detailed(root)