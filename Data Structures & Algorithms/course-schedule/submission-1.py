class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}
        for n1,n2 in prerequisites:
            premap[n1].append(n2)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False

            if premap[crs] == []:
                return True
            visit.add(crs)
            for n in premap[crs]:
                if not dfs(n):
                    return False
            visit.remove(crs)
            premap[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True