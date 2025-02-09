from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        """
        Brainstorming
        rect - brick - wall
        n rows of brick
        ith row of wall has bricks
            same height
            but may varies in width
            but all row has same width
        Task:
        draw vertical line from top to bottom
            cross the least bricks
            brick is not considered as crossed if the line goes through the
            edge of a brick
        return minimum number of crossed bricks after drawing the line

        Input:
        wall
        [
            [1,11,11,1],
            [111 ,1,11],
            [1,111, 11],
            [11,1111],
            [111,1,11],
            [1,111,1,1]
        ]

        after every brick there is gap
        store that gap indexes for each row

        0, 1, 2, 3, 4, 5
        1, 1, 1, 1, 1, 1
        1, 1, 1, 1, 1, 1
        1, 1, 1, 1, 1, 1

        {
            0: 6,
            1: 3,
            2: 1,
            3: 3,
            4: 4,
            5: 2,
            6: 6,
        }
        """

        # # case single row and more than 1 column
        if len(wall) == 1 and len(wall[0]) > 1:
            return 0

        wall_brick_ends = []

        for row in wall:
            row_brick_ends = []
            row_brick_ends.append(0)
            for idx in range(len(row)):
                row_brick_ends.append(sum(row[: idx + 1]))
            row_brick_ends.append(sum(row))
            wall_brick_ends.append(set(row_brick_ends))

        if len(wall_brick_ends) == 0:
            return 0

        ends_hash_map = {}

        for row_brick_ends in wall_brick_ends:
            for brick_ends in row_brick_ends:
                if brick_ends in ends_hash_map:
                    ends_hash_map[brick_ends] += 1
                else:
                    ends_hash_map[brick_ends] = 1

        greater = float("-inf")

        for indices in ends_hash_map:
            if indices == 0:
                continue
            if indices == sum(wall[0]):
                continue
            if ends_hash_map[indices] > greater:
                greater = ends_hash_map[indices]

        if greater == float("-inf"):
            return len(wall)

        return len(wall) - greater


if __name__ == "__main__":
    s = Solution()
    wall = [
        [1, 2, 2, 1],
        [3, 1, 2],
        [1, 3, 2],
        [2, 4],
        [3, 1, 2],
        [1, 3, 1, 1],
    ]
    print(s.leastBricks(wall))
    wall = [[1], [1], [1]]
    print(s.leastBricks(wall))
    wall = [[100000000], [100000000], [100000000]]
    print(s.leastBricks(wall))
    wall = [[1, 1], [2], [1, 1]]
    print(s.leastBricks(wall))
    wall = [[1, 1], [1, 1], [1, 1]]
    print(s.leastBricks(wall))
    wall = [[1, 1], [1, 1], [1, 1], [1, 1]]
    print(s.leastBricks(wall))
    wall = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]
    print(s.leastBricks(wall))
    wall = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]
    print(s.leastBricks(wall))
    wall = [[2147483647, 2147483647, 2147483647, 2147483647]]
    print(s.leastBricks(wall))
    wall = [[1]]
    print(s.leastBricks(wall))
    wall = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    print(s.leastBricks(wall))
    wall = [[1, 1], [2], [1, 1]]
    print(s.leastBricks(wall))
