class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even1 = [0] * 26
        even2 = [0] * 26

        odd1 = [0] * 26
        odd2 = [0] * 26

        for i in range(len(s1)):
            if i % 2 == 0:
                even1[ord(s1[i]) - ord('a')] += 1
                even2[ord(s2[i]) - ord('a')] += 1
            else:
                odd1[ord(s1[i]) - ord('a')] += 1
                odd2[ord(s2[i]) - ord('a')] += 1

        return even1 == even2 and odd1 == odd2


# Driver Code
if __name__ == "__main__":
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")

    sol = Solution()
    result = sol.checkStrings(s1, s2)

    print("Can the strings be made equal?", result)