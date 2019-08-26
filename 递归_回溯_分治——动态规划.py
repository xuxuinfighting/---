"""leetcode 第17 题 电话号码字母组合"""
def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}
            
    def backtrack(combination, next_digits):
        # if there is no more digits to check
        if len(next_digits) == 0:
            # the combination is done
            output.append(combination)
        # if there are still digits to check
        else:
            # iterate over all letters which map 
            # the next available digit
            for letter in phone[next_digits[0]]:
                # append the current letter to the combination
                # and proceed to the next digits
                backtrack(combination + letter, next_digits[1:])
                
    output = []
    if digits:
        backtrack("", digits)
    return output

"""leetcode 第46题 全排列"""
def permute(nums):
    if len(nums) == 0:
        return []

    used = [False] * len(nums)
    res = []
    __dfs(nums, 0, [], used, res)
    return res

def __dfs(nums, index, pre, used, res):
    # 先写递归终止条件
    if index == len(nums):
        res.append(pre.copy())
        return

    for i in range(len(nums)):
        if not used[i]:
            # 如果没有用过，就用它
            used[i] = True
            pre.append(nums[i])
            # 在 dfs 前后，代码是对称的
            __dfs(nums, index + 1, pre, used, res)
            used[i] = False
            pre.pop()

"""leetcode 第132题 分割回文串"""
TODO
"""leetcode 第41题 正则表达式匹配"""
TODO
"""leetcode 第64题 最小路径和"""
def minPathSum(grid:List[List[int]]) -> int :
	if not grid : return 0
	row = len(grid)
	col = len(grid[0])
	dp = [[0] * col for _ in range(row)]
	#第一行
	for j in range(1,col) :
		dp[0][j] = dp[0][j-1] + grid[0][j]
	#第一列
	for i in range(1,row) :
		dp[i][0] = dp[i-1][0] + grid[i][0]

	for i in range(1,row) :
		for j in range(1,col) :
			dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
	return dp[-1][-1]

"""leetcode 第322题 零钱兑换"""
def coinChange(coins: List[int], amount: int) -> int:
        max_size = amount + 1
        dp = [max_size] * max_size
        dp[0] = 0
        for i in range(1,max_size) :
            for c in coins :
                if i >= c:
                    tmp = dp[i-c] + 1
                    dp[i] = min(tmp,dp[i])
                
        if dp[amount] <max_size :
            return dp[amount]
        else :
            return -1
"""leetcode 第121题 买卖股票最佳时机"""
 def maxProfit(prices: List[int]) -> int:
        # cost_list = [max(prices) for i in range(prices)]
        # cost_list[0] = 
        if len(prices) == 0:
            return 0
        cost = prices[0]
        profit = 0
        for i in range(len(prices)) :
            cost = min(prices[i],cost)
            profit = max(profit,prices[i] - cost)
        return profit
"""leetcode 第152题 乘积最大子序列"""

 def maxProduct(self, nums: List[int]) -> int:
        mi = ma = res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0: mi, ma = ma, mi
            ma = max(ma * nums[i], nums[i])
            mi = min(mi * nums[i], nums[i])
            res = max(res, ma)
        return res 

"""leecode 第120题 三角形最小路径和"""

def minimumTotal(triangle):
	row = len(triangle) - 2
	for row in range(row,-1,-1) :
		for col in range(len(triangle[row])) :
			triangle[row][col] += min(triangle[row + 1][col],triangle[row + 1][col] + 1)
	return triangle[0][0]