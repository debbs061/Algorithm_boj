# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # pre-order traversal
    def serialize(self, root):
        ser = []

        def dfs(node):
            if not node:
                ser.append("N")
                return
            ser.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(ser)

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(vals[self.i])
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

    # Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
