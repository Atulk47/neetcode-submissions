class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        INF = 2147483647

        def bfs(q,r,c):
            dist = 0
            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    for dr,dc in dirs:
                        r1=dr+r
                        c1=dc+c

                        if (r1 in range(rows)) and (c1 in range(cols)) and grid[r1][c1] == INF:
                            grid[r1][c1] = dist+1
                            q.append((r1,c1))
                dist+=1
            return dist

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
        bfs(q,i,j)