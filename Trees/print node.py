
class Trees:
    def __init__(self, value):
        self.data = value
        self.children = []

root = Trees(1)

child1 = Trees(2)
child2 = Trees(3)
child3 = Trees(4)

root.children.append(child1)
root.children.append(child2)
root.children.append(child3)

def print_tree(root):
    print(root.data)
    for child in root.children:
        print_tree(child)

print_tree(root)

def print_tree_detailed(root):
    if(root==None): # Edge Case
        return
    
    print(f"{root.data}:",end = "")

    for eachChild in root.children:
        print(eachChild.data,end = ",")

    print()

    for eachChild in root.children:
        print_tree_detailed(eachChild)

print_tree_detailed(root)