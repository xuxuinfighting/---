'''
【栈】
用数组实现一个顺序栈
用链表实现一个链式栈
编程模拟实现一个浏览器的前进、后退功能（选做）
【队列】
用数组实现一个顺序队列
用链表实现一个链式队列
实现一个循环队列
【递归】
- 编程实现斐波那契数列求值 f(n)=f(n-1)+f(n-2)
- 编程实现求阶乘 n!
- 编程实现一组数据集合的全排列
'''


""" 数组实现栈"""
class MyStack(object):
    """模拟栈"""

    def __init__(self):
        self.items = []

    def is_empty(self):
        """判断是否为空"""
        return self.items == []

    def size(self):
        """返回栈的大小"""
        return len(self.items)

    def push(self, item):
        """压栈(加入元素)"""
        self.items.append(item)


    def pop(self):
        """弹栈(弹出元素)"""
        if len(self.items)>0:
            return self.items.pop()
        else:
            print("栈已经为空")
            return None

    def top(self):
        """返回栈顶元素"""
        if not self.is_empty():
            return self.items[len(self.items) - 1]
        else:
            return None

"""用链表实现一个链式队列"""
class LNode(object):
    def __init__(self,x):
        self.data = x
        self.next = None

class MyQueue(object):
    def __init__(self):
        """分配头结点"""
        self.pHead = None
        self.pEnd = None

    def is_empty(self):
        """判断是否为空"""
        if self.pHead == None:
            return True
        return False

    def size(self):
        """获取队列的大小"""
        size=0
        p = self.pHead
        while p != None:
        # while p is not None:
            p = p.next
            size += 1
        return size

    def enQueue(self, element):
        """入队列，从队尾加"""
        p = LNode(element)
        p.data = element
        p.next = None
        if self.pHead == None:
            self.pHead = self.pEnd=p
        else:
            self.pEnd.next = p
            self.pEnd = p

    def deQueue(self):
        """出队列，删除首元素"""
        if self.pHead == None:
            print("出队列失败，队列已经为空")
        self.pHead = self.pHead.next
        if self.pHead == None:
            self.pEnd = None

    def getFront(self):
        """返回队列首元素"""
        if self.pHead == None:
            print("获取队列首元素失败，队列已经为空")
            return None
        return self.pHead.data

    def getBack(self):
    	"""返回队列尾元素"""
        if self.pEnd == None:
            print("获取队列尾元素失败，队列已经为空")
            return None
        return self.pEnd.data


"""leetcode 第20 题 有效的括号"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        dic={')':'(','}':'{',']':'['}       #使用字典存储括号,并且右括号为key,左括号为value
        for char in  s :
            if char in dic.values() :
                stack.append(char)
            elif char in dic.keys() :
                if stack == [] or dic[char] != stack.pop():
                    return False
            else :
                return False
        return stack==[] 

"""leetcode 第32题 最长有效括号"""
def longestValidParentheses(s):
        l = 0
        stack = []
        start = 0
        dic = {')':'('}
        for i in range(len(s)):
            if s[i] in dic.values():
                stack.append(s[i])
            elif s[i] in dic.keys():
                if stack == []:
                    i += 1
                    continue
                if s[i] != stack.pop():
                    l += 2
                   
            else :
                return 0
            i += 1
        return l

"""leetcode 第150题 逆波兰表达式求值"""
def evalRPN(tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = list()
        oper = ['+', '-', '*', '/']
        for char in tokens:
            if char not in oper:
                stack.append(int(char))
            else:
                top1 = stack.pop()
                top2 = stack.pop()
                if char == '+':
                    stack.append(top2 + top1)
                elif char == '-':
                    stack.append(top2 - top1)
                elif char == '*':
                    stack.append(top2 * top1)
                elif char == '/':
                    stack.append(int(top2 / top1))

        return stack.pop()

"""leetcode 第641题 设计一个双端队列"""
TODO

"""leetcode 第239题  滑动窗口最大值"""
TODO

"""LeetCode 第70题 爬楼梯"""
def climbStairs(n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        if n == 1 or n == 2:
            return n
        pre = 2
        prepre = 1
        ret = 0
        for i in range(3, n+1):
            ret = pre + prepre
            prepre = pre
            pre = ret
        return ret