# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        graph = defaultdict(list)
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                queue.append(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                queue.append(node.right)
        def bfs(start):
            queue = deque([start])
            visited = set()
            visited.add(start)
            farthestNode = start
            diameter = -1
            while queue:
                n = len(queue)
                diameter += 1
                while n:
                    node = queue.popleft()
                    farthestNode = node
                    for neighbour in graph[node]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            queue.append(neighbour)
                    n -= 1
            return farthestNode,diameter
        farNode,_ = bfs(root)
        _,diameter = bfs(farNode)
        return diameter
                
                    
