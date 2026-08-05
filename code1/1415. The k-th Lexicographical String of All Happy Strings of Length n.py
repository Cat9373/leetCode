class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []

        def backtrack(path):
            if len(path) == n:
                ans.append("".join(path))
                return

            for ch in "abc":
                if not path or path[-1] != ch:
                    path.append(ch)
                    backtrack(path)
                    path.pop()

        backtrack([])

        if k > len(ans):
            return ""

        return ans[k - 1]


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter the length of the happy string (n): "))
    k = int(input("Enter the value of k: "))

    sol = Solution()
    result = sol.getHappyString(n, k)

    if result:
        print(f"The {k}-th happy string is: {result}")
    else:
        print("No such happy string exists.")