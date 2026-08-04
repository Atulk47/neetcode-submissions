class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1]*n

        def find(n1):
            r = n1
            while r != parent[r]:
                parent[r] = parent[parent[r]]
                r = parent[r]

            return r

        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                return 0

            elif rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2
            return 1
        res = n
        for n1,n2 in edges:
            res -= union(n1,n2)
        return res