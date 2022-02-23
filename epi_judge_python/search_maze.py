import collections
import copy
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple("Coordinate", ("x", "y"))


def search_maze(
    maze: List[List[int]], s: Coordinate, e: Coordinate
) -> List[Coordinate]:
    visited: Set[Coordinate] = set()

    def dfs(node, path):
        if node == e:  # destination reached
            return path

        if node in visited:
            return None

        visited.add(node)

        for succ in successors(maze, node):
            path.append(succ)
            result = dfs(succ, path)
            if result:
                return result
            del path[-1]  # more efficient than copying path for every dfs() call

    return dfs(s, [s])


def successors(maze, node):
    def isValid(cur):
        if (
            cur.x < 0
            or cur.x >= len(maze)
            or cur.y < 0
            or cur.y >= len(maze[0])
            or maze[cur.x][cur.y] == BLACK
        ):
            return False
        return True

    x, y = node
    succs = [
        Coordinate(x - 1, y),
        Coordinate(x + 1, y),
        Coordinate(x, y - 1),
        Coordinate(x, y + 1),
    ]
    return filter(isValid, succs)


def path_element_is_feasible(maze, prev, cur):
    if not (
        (0 <= cur.x < len(maze))
        and (0 <= cur.y < len(maze[cur.x]))
        and maze[cur.x][cur.y] == WHITE
    ):
        return False
    return (
        cur == (prev.x + 1, prev.y)
        or cur == (prev.x - 1, prev.y)
        or cur == (prev.x, prev.y + 1)
        or cur == (prev.x, prev.y - 1)
    )


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_maze.py", "search_maze.tsv", search_maze_wrapper
        )
    )
