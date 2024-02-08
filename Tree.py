class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def dfs(self):
        results = [self.data]
        for child in self.children:
            results += child.dfs()
        return results


root = TreeNode("A")
node_b = TreeNode("B")
node_c = TreeNode("C")
node_d = TreeNode("D")
node_e = TreeNode("E")
node_f = TreeNode("F")
node_g = TreeNode("J")
node_h = TreeNode("H")
node_i = TreeNode("I")


root.add_child(node_b)
root.add_child(node_c)
root.add_child(node_d)
root.add_child(node_e)
root.add_child(node_f)
root.add_child(node_g)
root.add_child(node_h)
root.add_child(node_i)

print(root.dfs())