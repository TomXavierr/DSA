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

        