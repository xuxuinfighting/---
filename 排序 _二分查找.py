"""
【排序】
实现归并排序、快速排序、插入排序、冒泡排序、选择排序、堆排序（完成leetcode上的返回滑动窗口中的最大值(239)，这是上一期第三天的任务进行保留（涉及队列可以对第二天进行整理复习））
编程实现 O(n) 时间复杂度内找到一组数据的第 K 大元素
【二分查找】
实现一个有序数组的二分查找算法
实现模糊二分查找算法（比如大于等于给定值的第一个元素）
"""

#插入排序
"""
插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，但将最后一个元素除外（让数组多一个空间才有插入的位置），
而第二部分就只包含这一个元素（即待插入元素）。在第一部分排序完成后，再将这个最后元素插入到已排好序的第一部分中。
"""
def insert_sort(lists):
	count = len(lists)
	for i in range(1,count) :
		key = lists[i]
		j = i - 1
		while j >= 0 :
			if lists[j] > key :
				lists[j + 1] = lists[j]
				lists[j] = key
			j -= 1
		return lists


#冒泡排序
"""
重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
"""

def bubble_sort(lists) :
	for i in range(len(lists)) :
	for j in range(i + 1,len(lists)) :
		if lists[i] > lists[k] :
			lists[i],lists[j] = lists[j],lists[i]
	return lists


#选择排序
"""
第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，将它与r1交换；
第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，将它与r2交换；
以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕。
"""
def select_sort(lists) :
	for i in range(len(lists)) :
		min = i
		for j in range(i + 1,len(lists)) :
			if lists[min] > lists[j] :
				min = j
		lists[min],lists[i] = lists[i],lists[min]
	return lists


#归并排序
"""
将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。
若将两个有序表合并成一个有序表，称为二路归并。
"""
def merge(left,right) :
	i,j = 0,0
	result = []
	while i < len(left) and j < len(right) :
		if left[i] <= right[j] :
			result.append(left[i])
			i += 1
		else :
			result.append(right[j])
			j += 1
		result += left[i:]
		result += left[j:]
		return result

def merge_sort(lists) :
	if len(lists) <= 1 :
		return lists
	nums = len(lists) / 2
	left = merge_sort(lists[:nums])
	right = merge_sort(lists[nums:])
	return merge(left,right)


#快速排序
"""
通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
"""
def quick_sort(lists,left,right) :
	if left >= right :
		return lists
	key = lists[left]
	low = left
	high = right
	while left < right :
		while left < right and lists[right] >= key:
			right -= 1
		lists[left] = lists[right]
		while left < right and lists[left] <= key:
			left += 1
		lists[right] = lists[left]
	lists[right] = key
	quick_sort(lists,low,left - 1)
	quick_sort(lists,left + 1,high)
	return lists


#堆排序
"""
选择排序的一种。可以利用数组的特点快速定位指定索引的元素。
堆分为大根堆和小根堆，是完全二叉树。大根堆的要求是每个节点的值都不大于其父节点的值，即A[PARENT[i]] >= A[i]。
在数组的非降序排序中，需要使用的就是大根堆，因为根据大根堆的要求可知，最大的值一定在堆顶。
"""
def adjust_heap(lists,i,size) :
	lchild = 2 * i + 1
	rchild = 2 * i + 2
	max = i
	if i < size/2 :
		if lchild < size and lists[lchild] > lists[max] :
			max = lchild
		if rchild < size and lists[rchild] > lists[max] :
		    max = rchild
		 if max != i :
		 	lists[max],lists[i] = lists[i],lists[max]
		 	adjust_heap(lists,max,size)

def build_heap(lists,size) :
	for i in range(0,(size / 2))[::-1] :
		adjust_heap(lists,i,size)

def heap_sort(lists) :
	size = len(lists)
	bulid_heap(lists,size)
	for  i in range(0,size)[::-1]:
		lists[0],lists[i] = lists[i],lists[0]
		adjust_heap(lists,0,i)
		

#找到一组数据的第 K 大元素
"""方法1 快排思想，时间复杂度近似为O(n) """
def partition(num, low, high):
    pivot = num[low]
    while (low < high):
        while (low < high and num[high] > pivot):
            high -= 1
        while (low < high and num[low] < pivot):
            low += 1
        num[low],num[high] = num[high],num[low]
    num[high] = pivot
    return high,num

def findkth(num,low,high,k): #找到数据中第k个数
	index = partition(num,low,high)[0]
	if index == k :return num[index]
	if index < k :
		return findkth(num,index + 1 ,high,k)
	else :
		return findkth(num,low,index - 1,k)

"""方法2 堆排序  时间复杂度O(n * logk)"""
def heap_build(parent,heap) :
	child = 2 * parent + 1
	while child<len(heap) :
		if child < len(heap) and heap[child + 1] < heap[child] :
			child = child + 1
		if heap[parent] <= heap[child] :
			break
		heap[parent],heap[child] = heap[child],heap[parent]
		parent,child = child,2 * child + 1
	return heap
def Find_heap_kth(array,k) :
	if k > len(array) :
		return None
	heap = array[:k]
	for i in range(k,-1,-1) :
		heap_build(i,heap)
	for j in range(k,len(array)) :
		if array[j] > heap[0] :
			heap[0] = array[j]
			heap_build(0,heap)
	return heap[0]

#模糊二分查找
TODO

"""leetcode 第239题 滑动窗口最大值"""
def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
       if not nums:
            return []
        from collections import deque
        dq = deque()
        n = len(nums)
        ans = []

        for i in range(k-1):
            #把前k-1个元素入队
            while len(dq) > 0:
                if nums[dq[-1]] <= nums[i]:
                    dq.pop()
                else:
                    break
            dq.append(i)  

        for i in range(k-1, n):
            while len(dq) > 0:
                if nums[dq[-1]] <= nums[i]:
                    dq.pop()
                else:
                    break
            dq.append(i)

            while dq[0] < i-k+1:
                dq.popleft()
            ans.append(nums[dq[0]])

        return ans

"""leetcode 第69题 x 的平方根"""
"""方法1 二分法"""
def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    min ,max = 0,x
    mid = x // 2
    while min < = max :
         m = mid * mid
         if m > x :
         	max = mid -1
         elif m < x :
         	min = mid + 1
         else :
         	return mid
         	break
        mid = (min + max) //2
    return mid  
       min = 0
       max = x
        mid = x//2
        while min<=max:
            m = mid*mid
            if m>x:
                max = mid-1
            elif m<x:
                min = mid+1
            else:
                return mid
                break
            mid = (min+max)//2
        return mid  

"""牛顿法"""
def mySqrt(x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            raise Exception('不能输入负数')
        if x == 0:
            return 0

        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return cur
