"""leetcode 第15题 Three Sum"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        L, res = len(nums), []
        for i in range(L-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j,k = i + 1, L - 1
            while j<k:
                if nums[j]+nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j = j + 1
                    while j<k and nums[j] == nums[j-1]:
                        j = j + 1
                elif nums[j] + nums[k] < target:
                    j = j + 1
                else:
                    k = k - 1
        return res
    
"""leetcode 第169题 找众数"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}
        for i in nums:
        	if i in num_dict:
        		num_dict[i] += 1
        	else :
        		num_dict[i] = 1
        return max(num_dict.items(),key = lambda x : x[1])[0]

"""leetcode 第41题 寻找第一个丢失的正整数"""
TODO


"""leetcode 第141题 是否存在环形"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
 
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        p1=p2=head#p1每次跑1步，p2每次跑2步
        while p2.next and p2.next.next:#判断跑得快的是否为空
            p1=p1.next
            p2=p2.next.next
            if p1==p2:#存在环则必然会出现相等
                return True
        return False

"""leetcode 第23题 合并k个有序链表"""
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution(object):
    def mergeKLists(self,lists):
        if not lists:
            return None
        res = []
        for a in lists:
            res.append(a.val)
            a = a.next
         res.sort()
        p = ListNode(0)
        q = p
        for i in range(0,len(res)):
            q.next = ListNode(res[i])
            q = q.next
         return p.next
