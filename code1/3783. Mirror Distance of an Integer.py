def mirrorDistance(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10

    return abs(original - reverse)


# Test cases
print(mirrorDistance(25))  # 27
print(mirrorDistance(10))  # 9
print(mirrorDistance(7))   # 0