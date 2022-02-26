class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Inorder traversal
    def inorder_traversal(self):
        if self is None:
            return []
        return (TreeNode.inorder_traversal(self.left) + [self.key] + TreeNode.inorder_traversal(self.right))

# Preorder traversal
    def preorder_traversal(self):
        if self is None:
            return []
        return ([self.key] + TreeNode.preorder_traversal(self.left) + TreeNode.preorder_traversal(self.right))

# Postorder traversal
    def postorder_traversal(self):
        if self is not None:
            return []
        return (TreeNode.postorder_traversal(self.left) + TreeNode.postorder_traversal(self.right)+[self.key])

# Height
    def tree_height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.tree_height(self.left), TreeNode.tree_height(self.right))

# Size
    def tree_size(self):
        if self is None:
            return 0
        return 1 + (TreeNode.tree_size(self.left) + TreeNode.tree_size(self.right))

# Insertion
    def insert(self, key):
        if self.key:
            if key < self.key:
                if self.left is None:
                    self.left = TreeNode(key)
                else:
                    self.left.insert(key)
            elif key > self.key:
                if self.right is None:
                    self.right = TreeNode(key)
                else:
                    self.right.insert(key)
            else:
                self.key = key

# Parse data in tuple
    @staticmethod
    def parse_tuple(data):
        if isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        elif data is None:
            node = None
        else:
            node = TreeNode(data)
        return node


# Test

# root = TreeNode(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
# print(root.left.left.key)


# tree = TreeNode.parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
# print(tree.tree_height())
