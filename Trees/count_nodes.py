from common import *
def count_node(root):
    if root == None:
        return 0
    
    answer = 1

    for child in root.children:
        answer = answer + count_node(child)
    
    return answer

root = Tree(1)

child1 = Tree(2)
child2 = Tree(3)
child3 = Tree(4)

root.children.append(child1)
root.children.append(child2)
root.children.append(child3)

print(count_node(root))

def height_of_tree(root):
    if root == 0:
        return 0
    
    height = 1
    max_child_height = 0

    for each_child in root.children:
        max_child_height = max(max_child_height,height_of_tree(each_child))
    
    height = height + max_child_height

    return height
