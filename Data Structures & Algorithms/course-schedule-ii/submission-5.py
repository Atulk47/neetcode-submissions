class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i:[] for i in range(numCourses)}
        for n1,n2 in prerequisites:
            premap[n1].append(n2)

        cycle = set()
        visit = set()

        op = []

        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visit:
                return True

            cycle.add(crs)
            for n in premap[crs]:
                if not dfs(n):
                    return False
            op.append(crs)
            cycle.remove(crs)
            visit.add(crs)
            return True

        
        for n in range(numCourses):
            if not dfs(n):
                return []
        return op