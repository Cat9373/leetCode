class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return (
            sorted([s1[0], s1[2]]) == sorted([s2[0], s2[2]])
            and
            sorted([s1[1], s1[3]]) == sorted([s2[1], s2[3]])
        )


# Driver Code
if __name__ == "__main__":
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")

    sol = Solution()
    result = sol.canBeEqual(s1, s2)

    print("Can the strings be made equal?", result)