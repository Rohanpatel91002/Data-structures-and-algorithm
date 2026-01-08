from collections import deque
class Binary_Tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def take_input_levelwise():
    value = int(input("enter the value for the root node: "))
    root = Binary_Tree(value)
    
    queue = deque([root])

    while queue:

        current_node = queue.popleft()

        value = int(input(f"enter the value for the left node of {current_node.data}: "))
        if value != -1:
            left_node = Binary_Tree(value)
            current_node.left = left_node
            queue.append(left_node)
        
        value = int(input(f"enter the value for the right node of {current_node.data}: "))
        if value != -1:
            right_node = Binary_Tree(value)
            current_node.right = right_node
            queue.append(right_node)

    return root

def print_binary_tree(root):
    if root == None:
        return 
    
    print(root.data,end=": ")

    if root.left is not None:
        print(f"Left->{root.left.data}", end=', ')
    else:
        print(f"Left->None", end=', ')
    
    if root.right is not None:
        print(f"Right->{root.right.data}")
    else:
        print(f"Right->None")
    
    print_binary_tree(root.left)
    print_binary_tree(root.right)

print_binary_tree(take_input_levelwise())
        

