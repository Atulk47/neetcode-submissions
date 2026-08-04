class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh = 0
        visit = set()
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(q,r,c,fresh):
            mins = 0
            while q and fresh:
                for i in range(len(q)):
                    r,c = q.popleft()
                    for dr, dc in dirs:
                        r1 = r+dr
                        c1 = c+dc
                        if (r1 in range(rows)) and (c1 in range(cols)) and grid[r1][c1] == 1:
                            grid[r1][c1] = 2
                            fresh -= 1
                            q.append((r1,c1))
                mins+=1
            return mins,fresh


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        mins,fresh = bfs(q,r,c,fresh)
        if fresh == 0:
            return mins
        else:
            return -1

