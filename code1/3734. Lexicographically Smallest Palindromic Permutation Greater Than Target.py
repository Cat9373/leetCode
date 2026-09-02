def lexPalindromicPermutation(s: str, target: str) -> str:
    n = len(s)

    # Count characters
    count = [0] * 26

    for ch in s:
        count[ord(ch) - ord('a')] += 1

    # A palindrome can have at most one odd-frequency character
    middle = ""

    for i in range(26):
        if count[i] % 2 == 1:
            if middle:
                return ""
            middle = chr(ord('a') + i)

    # Characters available for the left half
    half_count = [x // 2 for x in count]
    half_len = n // 2

    target_half = target[:half_len]

    # Try to match target's left half
    remaining = half_count[:]
    prefix = []

    mismatch = -1

    for i in range(half_len):
        c = ord(target_half[i]) - ord('a')

        if remaining[c] > 0:
            remaining[c] -= 1
            prefix.append(target_half[i])
        else:
            mismatch = i
            break

    # Build the palindrome after choosing a larger character
    def make_palindrome(prefix, pos, char_index, remaining):
        remaining[char_index] -= 1

        suffix = []

        for c in range(26):
            suffix.extend(
                [chr(ord('a') + c)] * remaining[c]
            )

        half = (
            ''.join(prefix[:pos])
            + chr(ord('a') + char_index)
            + ''.join(suffix)
        )

        return half + middle + half[::-1]

    # We matched the entire target half
    if len(prefix) == half_len:

        half = ''.join(prefix)

        candidate = (
            half
            + middle
            + half[::-1]
        )

        if candidate > target:
            return candidate

        mismatch = half_len

    # Try making the first mismatching position larger
    if mismatch < half_len:

        target_char = ord(target_half[mismatch]) - ord('a')

        for c in range(target_char + 1, 26):

            if remaining[c] > 0:

                return make_palindrome(
                    prefix,
                    mismatch,
                    c,
                    remaining[:]
                )

    # Backtrack through the matched prefix
    for pos in range(len(prefix) - 1, -1, -1):

        # Restore the character used at this position
        old = ord(prefix[pos]) - ord('a')
        remaining[old] += 1

        target_char = ord(target_half[pos]) - ord('a')

        # Try the smallest character greater than target[pos]
        for c in range(target_char + 1, 26):

            if remaining[c] > 0:

                return make_palindrome(
                    prefix,
                    pos,
                    c,
                    remaining[:]
                )

    return ""


# -------------------------
# Test cases
# -------------------------

print(lexPalindromicPermutation("baba", "abba"))
# baab

print(lexPalindromicPermutation("baba", "bbaa"))
# ""

print(lexPalindromicPermutation("abc", "abb"))
# ""

print(lexPalindromicPermutation("aac", "abb"))
# aca

print(lexPalindromicPermutation("bb", "aa"))
# bb