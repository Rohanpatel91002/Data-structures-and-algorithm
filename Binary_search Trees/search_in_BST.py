class BST:
    def __init__(self, Value):
        self.data = Value
        self.left = None
        self.right = None

def search_BST(root, value):
    if root is None:
        return False

    if root.data == value:
        return True

    if value < root.data:
        return search_BST(root.left, value)
    else:
        return search_BST(root.right, value)

    
def get_BST_example():  

    root = BST(40)

    child1 = BST(10)
    child2 = BST(30)
    child3 = BST(5)
    child4 = BST(50)
    child5 = BST(60)

    child6 = BST(20)
    child7 = BST(70)
    child8 = BST(15)
    child9 = BST(25)
    child10 = BST(35)

    child11 = BST(45)
    child12 = BST(55)
    child13 = BST(65)
    child14 = BST(75)   # fixed duplicate name


    root.left = child1
    root.right = child2

    child1.left = child3
    child1.right = child4

    child2.left = child5    

    root.left = child2      # 30
    root.right = child4     # 50

    child2.left = child1    # 10
    child2.right = child10  # 35

    child1.left = child3    # 5
    child1.right = child6   # 20

    child6.left = child8    # 15
    child6.right = child9   # 25

    child4.left = child11   # 45
    child4.right = child5   # 60

    child5.left = child12   # 55
    child5.right = child7   # 70

    child7.left = child13   # 65
    child7.right = child14  # 75

    return root 

# print(search_BST(root, 56))