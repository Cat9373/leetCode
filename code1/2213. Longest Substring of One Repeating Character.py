class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)

        # Node:
        # (left_char, right_char, prefix, suffix, best, length)
        tree = [None] * (4 * n)

        def merge(a, b):
            if a is None:
                return b

            if b is None:
                return a

            left_char = a[0]
            right_char = b[1]

            prefix = a[2]
            suffix = b[3]
            best = max(a[4], b[4])

            if a[1] == b[0]:
                combined = a[3] + b[2]
                best = max(best, combined)

                # Entire left segment is the same character
                if a[2] == a[5]:
                    prefix = a[5] + b[2]

                # Entire right segment is the same character
                if b[3] == b[5]:
                    suffix = a[3] + b[5]

            return (
                left_char,
                right_char,
                prefix,
                suffix,
                best,
                a[5] + b[5]
            )

        def build(node, left, right):
            if left == right:
                tree[node] = (
                    s[left],
                    s[left],
                    1,
                    1,
                    1,
                    1
                )
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, left, right, index, char):
            if left == right:
                tree[node] = (
                    char,
                    char,
                    1,
                    1,
                    1,
                    1
                )
                return

            mid = (left + right) // 2

            if index <= mid:
                update(node * 2, left, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, right, index, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        answer = []

        for char, index in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, index, char)
            answer.append(tree[1][4])

        return answer


# Driver Code
if __name__ == "__main__":
    s = input("Enter string: ")
    queryCharacters = input("Enter query characters: ")
    queryIndices = list(map(int, input("Enter query indices: ").split()))

    sol = Solution()

    result = sol.longestRepeating(
        s,
        queryCharacters,
        queryIndices
    )

    print("Answer:", result)