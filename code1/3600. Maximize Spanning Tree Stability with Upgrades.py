class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.cnt = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return False

        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa

        self.parent[pb] = pa
        self.size[pa] += self.size[pb]
        self.cnt -= 1
        return True


class Solution:
    def maxStability(self, n: int, edges, k: int) -> int:
        uf = UnionFind(n)
        mn = 10 ** 9

        # Process mandatory edges
        for u, v, s, must in edges:
            if must:
                mn = min(mn, s)
                if not uf.union(u, v):
                    return -1

        # Check if graph can be connected
        for u, v, _, _ in edges:
            uf.union(u, v)

        if uf.cnt != 1:
            return -1

        if mn == 10 ** 9:
            mn = max(s * 2 for _, _, s, _ in edges)

        def check(limit):
            uf = UnionFind(n)

            # Use edges already strong enough
            for u, v, s, _ in edges:
                if s >= limit:
                    uf.union(u, v)

            rem = k

            # Upgrade eligible edges if needed
            for u, v, s, must in edges:
                if must:
                    continue
                if rem > 0 and s * 2 >= limit:
                    if uf.union(u, v):
                        rem -= 1

            return uf.cnt == 1

        lo, hi = 1, mn

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter the number of nodes: "))
    m = int(input("Enter the number of edges: "))

    print("Enter each edge as: u v strength must(0/1)")
    edges = []

    for i in range(m):
        u, v, s, must = map(int, input(f"Edge {i + 1}: ").split())
        edges.append([u, v, s, must])

    k = int(input("Enter the maximum number of upgrades (k): "))

    sol = Solution()
    result = sol.maxStability(n, edges, k)

    print("Maximum Stability:", result)