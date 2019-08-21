"""
1. 实现有向图、无向图、有权图、无权图的邻接矩阵和邻接表表示方法
2. 实现图的深度优先搜索、广度优先搜索实现
3. Dijkstra 算法实现
4. 拓扑排序
"""

#实现图的深度优先搜索、广度优先搜索实现
from cllections import deque
class Graph :
	"""无向图"""
	def __init__(self,num_vertices):
		self._num_vertices = num_vertices
		self._adjacency = [[] for _ in range(num_vertices)]
	def add_edge(self,s,t) :
		self._adjacency[s].append(t)
		self._adjacency[t].append(s)
	def _generate_path(self,s,t,prev) :
		if prev[t] or s != t :
			yield from self._generate_path(s,prev[t],prev)
		yield str(t)
	def bfs(self,s,t) :
		"""通过广度优先搜索s -> t的路径"""
		visited = [False] * self._num_vertices
		visited[s] = True
		q = deque()
		q.append(s)
		prev = [None] * self._num_vertices
		while q :
			v = q.popleft()
			for neighbour in self._adjacency[v] :
				if not in visited[neighbour] :
					prev[neighbour] = v
					if neighbour == t :
						print ('->'.join(self._generate_path(s,t,prev)))
						return 
					visited[neighbour] = True
					q.append(neighbour)

	def dfs (self,s,t) :
		found = False
		visited = [False] * self._num_vertices
		prev = [None] * self._num_vertices
		def _dfs(from_vertex) = True :
			nonlocal found
			if found :
				return 
			visited[from_vertex] = True
			if from_vertex == t :
				found = True
				return
			for neighbour in self._adjacency[from_vertex] :
				if not visited[neighbour] :
					prev[neighbour] = from_vertex
					_dfs(neighbour)
		_dfs(s)
		print ('->'.join(self._generate_path(s,t,prev)))
    
#Dijkstra 算法实现
def Dijkstra(G,start) :
	start = start
	inf = float("inf")
	node_num = len(G)
	visited = [0] * node_num
	dis = {node:G[start][node] for node in range(node_num)}
	parents = {node : -1 for node in range(node_num)}
	visited[start] = 1
	last_point = start
	for i in range(node_num - 1) :
		min_dis = dis[j]
		last_point = j
	 visited[last_point] = 1
        if i == 0:
            parents[last_point] = start
        for k in range(node_num):  # 利用新基准节点更新dis和parents列表的值
            if G[last_point][k] < inf and dis[k] > dis[last_point] + G[last_point][k]:
                dis[k] = dis[last_point] + G[last_point][k]
                parents[k] = last_point
    return {key: values for key, values in dis.items()}, {key: values for key, values in parents.items()}

"""leetcode 第 200题 岛屿的个数"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        row = len(grid)
        col = len(grid[0])
        cnt = 0

        def dfs(i, j):
            grid[i][j] = "0"
            for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == "1":
                    dfs(tmp_i, tmp_j)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i, j)
                    cnt += 1
        return cnt

                
"""leetcode 第 36题 有效数独"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3 ) * 3 + j // 3
                    
                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    
                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False         
        return True