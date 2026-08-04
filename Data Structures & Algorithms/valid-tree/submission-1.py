class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parents = [i for i in range(n)]
        rank = [1]*n

        if len(edges)!=n-1:
            return False

        def find(n1):
            res = n1
            while res != parents[res]:
                parents[res] = parents[parents[res]]
                res = parents[res]
            return res

        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                return False

            elif rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                parents[p2] = p1
            else:
                rank[p2]+=rank[p1]
                parents[p1] = p2
            return True
        for n1,n2 in edges:
            if not union(n1,n2):
                return False
        return True
            