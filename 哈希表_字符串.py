"""
【散列表（哈希表）】
实现一个基于链表法解决冲突问题的散列表
实现一个 LRU 缓存淘汰算法
【字符串】
实现一个字符集，只包含 a～z 这 26 个英文字母的 Trie 树
实现朴素的字符串匹配算法
"""


#基于链表法解决冲突
class ListNode :
	def __init__(self,value,pnext = None) :
		self.data = value
		self.next = pnext
class HashTable(object):
	"""docstring for HashTable"""
	def __init__(self, p):
		self.array = [None] * p
		self._div = p

	def hashFun(self,key) :
		#选择除法留余作为哈希函数
		return key % self._div
	def insert(self,value) :
		key = self.hashFun(value)
		if self.array[key] is None :
			self.array[key] = ListNode(None)
			node = ListNode(value)
		    self.array[key].next = node
		 else :
		 	node = ListNode(value)
		 	node.next = self.array[key].next
		 	self.array[key].next = node

	def showTable(self) :
		for index in range(self._div) :
			if self.array[index] :
				p = self.array[index].next
				while p :
					p = p.next




"""leetcode第1题 两数之和"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = dict()
        for i, x in enumerate(nums):
            if target - x in hash_map:
                return [i, hash_map[target-x]]
            hash_map[x] = i

"""leetcode 第344题 反转字符串"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        return s[::-1]

"""leetcode 第151题 翻转字符串里的单词"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return  ' '.join(s.split()[::-1]).strip()

"""leetcode 第8 题 字符串转换整数 (atoi)"""
TODO