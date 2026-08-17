class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        length = n + m - 1

        # Start with the lexicographically smallest characters
        word = ['a'] * length

        # fixed[i] tells whether this position is forced by a T
        fixed = [False] * length

        # Step 1: Apply all T constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    pos = i + j

                    # Conflicting T constraints
                    if fixed[pos] and word[pos] != str2[j]:
                        return ""

                    word[pos] = str2[j]
                    fixed[pos] = True

        # Step 2: Handle F constraints
        for i in range(n):
            if str1[i] == 'F':

                # Check whether this substring currently equals str2
                same = True

                for j in range(m):
                    if word[i + j] != str2[j]:
                        same = False
                        break

                # Already different
                if not same:
                    continue

                # Need to change one non-fixed position
                pos = -1

                # Choose the rightmost free position
                for j in range(m - 1, -1, -1):
                    if not fixed[i + j]:
                        pos = i + j
                        break

                # All positions are forced
                if pos == -1:
                    return ""

                # Make it different from str2[j]
                j = pos - i

                if str2[j] == 'a':
                    word[pos] = 'b'
                else:
                    word[pos] = 'a'

        return ''.join(word)


# Driver Code
if __name__ == "__main__":
    str1 = input("Enter str1: ")
    str2 = input("Enter str2: ")

    sol = Solution()
    result = sol.generateString(str1, str2)

    print("Generated string:", result)