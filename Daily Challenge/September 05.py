class Solution(object):
    def levelOrder(self, root):
        if not root:return []
        res = []
        stack = [root]
        while stack:
            temp = []
            next_stack = []
            for node in stack:
                temp.append(node.val)
                for child in node.children:
                    next_stack.append(child)
            stack = next_stack
            res.append(temp)
        return res
