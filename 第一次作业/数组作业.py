'''
【数组】 
1.实现一个支持动态扩容的数组，支持增删改操作
2.实现两个有序数组合并为一个有序数组
3.学习哈希表思想，并完成leetcode上的两数之和(1)及Happy Number(202)
'''
class Array:
	def __init__(self,capacity):
		self._capacity = capacity #数据最大容量
		self._size = 0 #数据已使用大小
		self._data = [None] * self._capacity #初始化元素

	def add(self,index,elem) :
		"""
        向数组中添加新的元素
		"""
		if (index < 0 or index > self._size) :
			print ("index不合法!")
			return 
		if (self._size == self._capacity) :
			self._resize(self._capacity * 2)
		for i in range(slef.size - 1,index - 1,-1) :
			self._data[i+1] = self._data[i]
		self._data[index] = elem
		self._size += 1
		def _resize(self,new_capacity) :
			newarr = Array(new_capacity)
			for i in range(self._size) :
				newarr._capacity = new_capacity
				for i in range(self._size) :
					newarr.add(i,self._data[i])
			self._capacity = new_capacity
			self._data = newarr._data

		def delete(self,index) :
			if index < 0 or index > self._size - 1 :
				print ("index不合法！删除失败")
			for i in range(index + 1,self._size,1) :
				self._data[i-1] = self._data[i]
			self._size -= 1

		def modify(self,index,new_value) :
			if index < 0 or index >self._size:
				print("index 不合法！修改失败") 
			self._data[index] = new_value

        def merge(self,sorted_list1,sorted_list2):
        	result = []
        	len1 = len(sorted_list1)
        	len2 = len(sorted_list2)
        	i = 0
        	j = 0
        	while i <len1 and j < len2 :
        		if sorted_list1[i] < sorted_list2[j]:
        			result.append(sorted_list1[i])
        			i += 1
        		else :
        			result.append(sorted_list2[j])
        			j += 1
            if i <len1:
            	for z in range(i+1,len1):
            		result.append(sorted_list1[z])
            elif j <len2:
            	for z in range(j+1,len2):
            		result.append(sorted_list2[z])
            return result

"""
leetcode 第一题 Two Sum
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    	wanted_nums = {}
        for i, num in enumerate(nums):
            if num in wanted_nums:
                return [wanted_nums[num], i] # dic[num] equals to i1, i = i2 -> [i1, i2]
            else: # if num not exist in dic
                wanted_nums[target - num] = i # add it in the dict


"""
leetcode 第202题 Happy Number
"""
class Solution(object):
    def isHappy(self, n):
    	d = {}
    	whlile True :
    	l = map(int,list(str(n)))
    	m = 0
    	for i in l :
    		m += i ** 2
    	if m in d :
    		return False
    	if m == 1 :
    		return True
    	d[m] = m
    	n = m
    	