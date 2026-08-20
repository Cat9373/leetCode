class Solution:
    def robotSim(self, commands, obstacles):
        # 0 = North, 1 = East, 2 = South, 3 = West
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        # Convert obstacles to a set for O(1) lookup
        obstacle_set = set()

        for x, y in obstacles:
            obstacle_set.add((x, y))

        x = 0
        y = 0
        direction = 0

        max_distance = 0

        for command in commands:

            # Turn left
            if command == -2:
                direction = (direction - 1) % 4

            # Turn right
            elif command == -1:
                direction = (direction + 1) % 4

            # Move forward
            else:
                dx, dy = directions[direction]

                for _ in range(command):
                    next_x = x + dx
                    next_y = y + dy

                    # Stop this command if obstacle is encountered
                    if (next_x, next_y) in obstacle_set:
                        break

                    x = next_x
                    y = next_y

                    max_distance = max(
                        max_distance,
                        x * x + y * y
                    )

        return max_distance