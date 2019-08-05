"""
【链表】
实现单链表、循环链表、双向链表，支持增删操作
实现单链表反转
实现两个有序的链表合并为一个有序链表
实现求链表的中间结点
"""
class SingleNode(object) :
	def __init__(self,val):
		self.val = val
		self.next = None
"""单链表"""
class SingleLinkList(object) :
	def __init__(self) :
		self.__head = None

	def is_empty(self):
		return self.__head == None
    def length(self):
        cur = self.__head     # cur初始时指向头节点
        count = 0
        while cur != None:   # 尾节点指向None，当未到达尾部时, 将cur后移一个节点
            count += 1
            cur = cur.next
        return count

	def add(self,pos,val) :
		node = SingleNode(val)
		if pos <= 0:
			node.next = self.__head
			self.__head = node  #将链表的head指向新节点
		elif pos > (self.length() - 1):
			if self.is_empty():
				self.__head = node
			else :
				cur = self.__head
				while cur.next != None :
					cur = cur.next
				cur.next = node
		else :
			count = 0
			pre = self.__head
			while count < (pos - 1):
				count += 1
				pre = pre.next
			node.next = pre.next
			pre.next = node
	def delete(self,val) :
		cur = self.__head
		pre = None
		while cur != None:
			if cur.item == item:
				if not pre:
					self.__head = cur.next
				else :
					pre.next = cur.next
				break
			else :
				pre = cur
				cur = cur.next
"""单向循环链表"""
class  SinCyclinkedlist(object) :
	def __init__(self):
		self.__head = None
	def is_empty(self):
		self.__head = None
    def length(self):
        if self.is_empty():
            return 0
        count = 1
        cur = self.__head
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

	 def add(self,pos,val):
	 	node = SingleNode(val)
	 	if pos <= 0:
	 		if self.is_empty():
	 			self.__head = node
	 		else :
	 			node.next = self.__head
	 			cur = self.__head
	 			while cur.next != self.__head:
	 				cur = cur.next
	 			cur.next = node
	 			self.__head = node
	 	elif pos > (self.length() - 1) :
	 		if self.is_empty():
	 			self.__head = None
	 			node.next = self.__head
	 		else:
	 			cur = self.__head
	 			while cur.next != self.__head:
	 				cur = cur.next
	 			cur.next = node
	 			node.next = self.__head
 		else :
	 			cur = self.__head
	 			count = 0
	 			while count < (pos - 1):
	 				count += 1
	 				cur = cur.next
	 			node.next = cur.next
	 			cur.next = node

    def delete(self,val):
    	cur = self.__head
    	pre = None
    	while cur.next != None :
    		if cur.val == val :
    			if cur == self.__head : # 先判断此节点是否头结点
    				rear = self.__head
    				while rear.next != self.__head:
    					rear = rear.next
    				self.__head = cur.next
    				rear.next = self.__head
    			else :
    				pre.next = cur.next
    			return
    		else :
    			pre = cur
    			cur = cur.next
"""双向链表节点"""
class Node(object):
	def __init__(self,val):
		self.val = val
		self.next = None
		self.prev = None
"""双向链表"""
class DoubleLinkList(object):
	def __init__(self):
		self.__head = None
	def is_empty(self):
		return self.__head == None
	def length(self):
		cur = self.__head
		count = 0
		while cur != None:
			count += 1
			cur = cur.next
		return count
	def add (self,pos,val) :
		node = Node(val)
		if pos <= 0:
			if self.is_empty():
				self.__head = node
			else :
				node.next = self.__head
				self.__head.prev = node
				self.__head = node
		elif pos > (self.length() - 1):
			if self.is_empty():
				self.__head = node
		    else :
		    	cur = self.__head
		    	while cur.next != None:
		    		cur = cur.next
		    	cur.next = node
		        node.prev = cur
		else :
			count = 0
			while count < (pos - 1):
				count += 1
				cur = cur.next
			node.prev = cur
			node.next = cur.next
			cur.next.prev = node
			cur.next = node
	def delete(self,val):
		cur = self.__head
		while cur != None:
			if cur.val == val :
				if cur == self.__head :
					self.__head = cur.next
					if cur.next:
						cur.next.prev = None
				else :
					cur.prev.next = cur.next
					if cur.next:
						cur.next.prev = cur.prev
				break
			else :
				cur = cur.next






"""单链表反转"""
def reverse_linkedlist(head):
	if head == None or head.next == None :
		return head
	p1 = head
	p2 = head.next
	tmp = None #保存数据的临时变量
	while p2 :
		tmp = p2.next
		p2.next = p1
		p1 = p2
		p2 = tmp
	head.next = None
	return p1


"""两个有序的链表合并为一个有序链表"""
class solutionmergerTwoLists:
	def __init__(self, x):
		self.val = x
		self.next = None
	def mergerTwoLists(self,l1,l2):
		if l1 is None:
			return l2
		elif l2 is None:
			return l1
		listMerge = None
		if l1.val < l2.val:
			listMerge = l1
			listMerge.next = self.mergerTwoLists(l1.next,l2)
		else:
			listMerge = l2
			listMerge.next = self.mergerTwoLists(l2.next,l1)
		return listMerge


"""求链表的中间结点"""
class ListNode(object):
	"""docstring for ClassName"""
	def __init__(self, x):
		self.val = x
		self.next = None
	def middleNode(self,head):
		fast = slow = head
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
		return slow

