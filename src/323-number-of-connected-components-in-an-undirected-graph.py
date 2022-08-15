import collections


class Solution(object):
    # return the number of connected components in the graph
    def countComponents(self, n, edges):
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:  # already unioned
                return 0

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)  # if successfully unioned
        return res


a = Solution()
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(a.countComponents(n, edges))
