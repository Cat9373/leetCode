from collections import deque


def minMoves(classroom, energy):
    m = len(classroom)
    n = len(classroom[0])

    litter = []
    start = None

    # Find start and litter
    for i in range(m):
        for j in range(n):
            if classroom[i][j] == 'S':
                start = (i, j)

            elif classroom[i][j] == 'L':
                litter.append((i, j))

    k = len(litter)

    if k == 0:
        return 0

    # Assign a bit to every litter
    litter_id = {}

    for i in range(k):
        r, c = litter[i]
        litter_id[(r, c)] = i

    full_mask = (1 << k) - 1

    queue = deque()

    sr, sc = start

    # (row, col, collected_mask, remaining_energy)
    queue.append((sr, sc, 0, energy))

    visited = set()
    visited.add((sr, sc, 0, energy))

    moves = 0

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    while queue:

        for _ in range(len(queue)):

            r, c, mask, e = queue.popleft()

            # Everything collected
            if mask == full_mask:
                return moves

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Out of bounds
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                # Obstacle
                if classroom[nr][nc] == 'X':
                    continue

                # Cannot move with zero energy
                if e == 0:
                    continue

                new_energy = e - 1
                new_mask = mask

                # Collect litter
                if (nr, nc) in litter_id:
                    bit = litter_id[(nr, nc)]
                    new_mask |= 1 << bit

                # Reset energy
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                state = (
                    nr,
                    nc,
                    new_mask,
                    new_energy
                )

                if state not in visited:
                    visited.add(state)
                    queue.append(state)

        moves += 1

    return -1


# Examples

print(minMoves(["S.", "XL"], 2))
# 2

print(minMoves(["LS", "RL"], 4))
# 3

print(minMoves(["L.S", "RXL"], 3))
# -1