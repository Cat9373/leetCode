class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Store the last occurrence of each character
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i

        stack = []
        visited = set()

        for i, ch in enumerate(s):
            # Skip if already in the stack
            if ch in visited:
                continue

            # Remove larger characters if they appear later
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                visited.remove(stack.pop())

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)


# Driver Code
if __name__ == "__main__":
    s = input("Enter the string: ")

    sol = Solution()
    result = sol.smallestSubsequence(s)

    print("Smallest subsequence:", result)