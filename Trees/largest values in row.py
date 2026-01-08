from common import *

def largest_values(root):
    if root == None:
        return 0
    queue = deque([root])
    output = []
    while queue:
        
        max_value = 0

        for _ in range(len(queue)):
            current_node = queue.popleft()
            max_value = max(max_value, current_node.data)

            for child in current_node.children:
                queue.append(child)
        
        output.append(max_value)
    
    return output

root = Tree(1)

child1 = Tree(2)
child2 = Tree(3)
child3 = Tree(4)

root.children.append(child1)
root.children.append(child2)
root.children.append(child3)

child4 = Tree(5)
child5 = Tree(6)

child2.children.append(child4)
child3.children.append(child5)

print(largest_values(root))