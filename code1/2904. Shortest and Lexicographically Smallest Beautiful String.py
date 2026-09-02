def shortestBeautifulSubstring(s: str, k: int):

    ones = []

    # Store positions of all 1s
    for i, ch in enumerate(s):
        if ch == '1':
            ones.append(i)

    # Not enough 1s
    if len(ones) < k:
        return ""

    best = ""

    # Check every group of k consecutive 1s
    for i in range(len(ones) - k + 1):

        left = ones[i]
        right = ones[i + k - 1]

        candidate = s[left:right + 1]

        # First candidate
        if best == "":
            best = candidate

        # Shorter candidate
        elif len(candidate) < len(best):
            best = candidate

        # Same length, lexicographically smaller
        elif len(candidate) == len(best) and candidate < best:
            best = candidate

    return best


# Test cases

print(shortestBeautifulSubstring("100011001", 3))
# 11001

print(shortestBeautifulSubstring("1011", 2))
# 11

print(shortestBeautifulSubstring("000", 1))
# ""