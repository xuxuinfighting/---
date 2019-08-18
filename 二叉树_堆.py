"""
【二叉树】
实现一个二叉查找树，并且支持插入、删除、查找操作
实现查找二叉查找树中某个节点的后继、前驱节点
实现二叉树前、中、后序以及按层遍历
并完成leetcode上的验证二叉搜索树(98)及二叉树 层次遍历(102,107)！（选做）注：这个跟下面的习题有重复
【堆】
实现一个小顶堆、大顶堆、优先级队列
实现堆排序
利用优先级队列合并 K 个有序数组
求一组动态数据集合的最大 Top K
"""

#二叉查找树
class BinarySearchTree(object) :
	def __init__(self,data,left = None,right = None,parent = None) :
		self.data = data 
		self.left = left 
		self.right = right
		self.parent = parent

class BST(object):
	"""docstring for BST"""
	def __init__(self):
		self.root = None
		self.size = 0
	def length(self) :
		return self.size
	def find(self,key) :
		if self.root :
			result = self._find(key,self.root)
			if result :
				return result
			else :
				return None
		else :
			None

	def _find(self,key,node) :
		if not node :
		 	return None
		elif node.data == key :
			return node
		elif key < node.data :
			return self._find(key,node.left)
		else :
			return self._find(key,node.right)

    def insert(self,key) :
    	node = BinarySearchTree(key)
    	if not self.root :
    		self.root = node
    		self.size += 1
    	else :
    		currentNode = self.root
    		while True:
    			if key < currentNode.data :
    				if currentNode.left :
    					currentNode = currentNode.left
    				else :
    					currentNode.left = node
    					node.parent = currentNode
    					self.size += 1
    					break
    			elif key > currentNode.data :
    				if currentNode.right :
    					currentNode = currentNode.right
    				else :
    					currentNode.right = node
    					node.parent = currentNode
    					self.size += 1
    					break
    			else :
    				break

    def findMin(self) :
    	if self.root :
    		return self._findMin(self.root)
    	else :
    		return None
    def findMax(self) :
    	if self.root :
    		currentNode = self.root
    		while currentNode.right:
    			currentNode = currentNode.right
    		return currentNode
    	else :
    		return None
    
    def _findMin(self,node) :
    	if node :
    		currentNode = node
    		while currentNode.left:
    			currentNode = currentNode.left
    		return currentNode


    def delete(root,key) :
    	if root is None:
    		return None
    	if root.val == key :
    		if root.left is None :
    			return None
    		else :
    			root = root.right
    	elif root.right is None :
    		root = root.left
    	else :
    		buffer = None
    		tmp = root.right
    		while tmp.left is not None :
    			buffer = tmp
    			tmp = tmp.left
    		root.val,tmp.val = tmp.val,root.val
    		if buffer is None :
    			root.right = self.delete(tmp,key)
    		else :
    			buffer.left = self.delete(tmp,key)

        elif key < root.val :
        	root.left = self.delete(root.left,key)
        else :
        	root.right = self.delete(root.right,key)
        return root

#实现堆
TODO

"""leetcode第226题 反转二叉树"""
def invertTree( self,root: TreeNode) -> TreeNode:
        if not root :
            return
        else :
            root.left,root.right = root.right,root.left
            root.left = self.inverTree(root.left)
            root.right = self.invertTree(root.right)
        return root

"""leetcode第104题 二叉树最大深度"""
def maxDepth(self, root: TreeNode) -> int:
        depth = 1
        if not root :
            return 0
        else :
            if root.left is not None or root.right is not None :
                depth = max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1
            return depth

"""leetcode第98题 验证二叉搜索树"""
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res=[]
        self.search(root, res)
        for i in range(1,len(res)):
            print (res)
            if res[i]<=res[i-1]:
                return False
        return True
    
    def search(self, root, res):
        if root:
            self.search(root.left, res)
            res.append(root.val)
            self.search(root.right, res)


"""leetcode 第112题 路径总和"""
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if nor root :
            return False
        sum -= root.val
        if not root.left and not root.right :
            return sum == 0
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)