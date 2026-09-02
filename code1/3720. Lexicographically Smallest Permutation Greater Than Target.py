def lexGreaterPermutation(s: str, target: str) -> str:

    n = len(s)

    # Count characters in s
    count = [0] * 26

    for ch in s:
        count[ord(ch) - ord('a')] += 1

    remaining = count[:]
    prefix = []

    # Try to match target from left to right
    for i in range(n):

        t = ord(target[i]) - ord('a')

        # Match target[i]
        if remaining[t] > 0:
            remaining[t] -= 1
            prefix.append(target[i])
            continue

        # target[i] is unavailable.
        # Try the smallest character greater than target[i].
        for c in range(t + 1, 26):

            if remaining[c] > 0:

                remaining[c] -= 1

                suffix = []

                for x in range(26):
                    suffix.append(
                        chr(ord('a') + x) * remaining[x]
                    )

                return (
                    ''.join(prefix)
                    + chr(ord('a') + c)
                    + ''.join(suffix)
                )

        # No larger character is available here
        break

    # Backtrack
    for pos in range(len(prefix) - 1, -1, -1):

        # Restore the character at this position
        old = ord(prefix[pos]) - ord('a')
        remaining[old] += 1

        target_char = ord(target[pos]) - ord('a')

        # Try a character greater than target[pos]
        for c in range(target_char + 1, 26):

            if remaining[c] > 0:

                remaining[c] -= 1

                suffix = []

                for x in range(26):
                    suffix.append(
                        chr(ord('a') + x) * remaining[x]
                    )

                return (
                    ''.join(prefix[:pos])
                    + chr(ord('a') + c)
                    + ''.join(suffix)
                )

    return ""


# -------------------------
# Test cases
# -------------------------

print(lexGreaterPermutation("abc", "bba"))
# bca

print(lexGreaterPermutation("leet", "code"))
# eelt

print(lexGreaterPermutation("baba", "bbaa"))
# ""

print(lexGreaterPermutation("abc", "abc"))
# acb

print(lexGreaterPermutation("cba", "abc"))
# acb