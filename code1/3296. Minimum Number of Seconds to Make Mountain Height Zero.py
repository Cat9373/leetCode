class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:

        def canFinish(time):
            total = 0

            for w in workerTimes:
                lo, hi = 0, mountainHeight

                while lo < hi:
                    mid = (lo + hi + 1) // 2
                    if w * mid * (mid + 1) // 2 <= time:
                        lo = mid
                    else:
                        hi = mid - 1

                total += lo
                if total >= mountainHeight:
                    return True

            return False

        left = 0
        right = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        while left < right:
            mid = (left + right) // 2

            if canFinish(mid):
                right = mid
            else:
                left = mid + 1

        return left


# Driver Code
if __name__ == "__main__":
    mountainHeight = int(input("Enter the mountain height: "))

    n = int(input("Enter the number of workers: "))

    print("Enter the worker times separated by spaces:")
    workerTimes = list(map(int, input().split()))

    if len(workerTimes) != n:
        print(f"Error: Expected {n} worker times, but got {len(workerTimes)}.")
    else:
        sol = Solution()
        result = sol.minNumberOfSeconds(mountainHeight, workerTimes)

        print("Minimum Number of Seconds:", result)