class Solution:
    def minimumTotalDistance(self, robot, factory):

        robot.sort()
        factory.sort()

        n = len(robot)

        INF = 10**30

        # dp[i] = minimum cost to repair the first i robots
        # using the factories processed so far
        dp = [INF] * (n + 1)
        dp[0] = 0

        for position, limit in factory:

            new_dp = [INF] * (n + 1)

            for j in range(n + 1):

                if dp[j] == INF:
                    continue

                # Don't use this factory
                new_dp[j] = min(
                    new_dp[j],
                    dp[j]
                )

                # Use this factory for 1 to limit robots
                cost = 0

                for count in range(1, limit + 1):

                    if j + count > n:
                        break

                    robot_position = robot[j + count - 1]

                    cost += abs(
                        robot_position - position
                    )

                    new_dp[j + count] = min(
                        new_dp[j + count],
                        dp[j] + cost
                    )

            dp = new_dp

        return dp[n]


# Driver Code
if __name__ == "__main__":

    # Example:
    # Robot positions: 0 4 6
    # Factories:
    # 2 2
    # 6 2

    robot = list(
        map(
            int,
            input("Enter robot positions: ").split()
        )
    )

    number_of_factories = int(
        input("Enter number of factories: ")
    )

    factory = []

    print("Enter each factory as: position limit")

    for _ in range(number_of_factories):
        position, limit = map(
            int,
            input().split()
        )

        factory.append([position, limit])

    sol = Solution()

    result = sol.minimumTotalDistance(
        robot,
        factory
    )

    print("Minimum total distance:", result)