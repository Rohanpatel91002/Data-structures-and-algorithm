from collections import deque
class Binary_Tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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

root = Binary_Tree(1)

child1 = Binary_Tree(2)
child2 = Binary_Tree(3)
child3 = Binary_Tree(4)
child4 = Binary_Tree(5)
child5 = Binary_Tree(6)

root.left = child1
root.right = child2

child1.left = child3
child1.right = child4

child2.left = child5
print_binary_tree(root)

def print_binary_tree_levelwise(root):
    if root == None:
        return
    
    queue = deque([root])

    while queue:
        current_node = queue.popleft()
        print(current_node.data,end=": ")

        if current_node.left!= None:
            queue.append(current_node.left)
        
        if current_node.right!= None:
            queue.append(current_node.right)

    return root

print_binary_tree_levelwise(root)

