__author__ = 'rdhek'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def diameterOfBinaryTree(root):
        if root is None:
            return 0
        q=[]
        count = 0
        maxWidth=0
        q.insert(0,root)
        while(q!=[]):
            count = len(q)
            
            maxWidth = max(maxWidth,count)
            while count is not 0:

                count = count -1
                temp = q[0]

                q.pop()

                if temp.left is not None:
                    q.insert(0,temp.left)
                if temp.right is not None:
                    q.insert(0,temp.right)
        return maxWidth


root = TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
print diameterOfBinaryTree(root)