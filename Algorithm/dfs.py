# Each number shows which numbers we can go to
graph = {
    1: [2, 5],  # From 1, we can go to 2 or 5
    2: [3, 4],  # From 2, we can go to 3 or 4
    3: [6],  # From 3, we can go to 6
    4: [6],  # From 4, we can go to 6
    5: [6, 7],  # From 5, we can go to 6 or 7
    6: [8, 9],  # 6 is one possible destination
    7: [],
    8: [11, 12],
    9: [10],
    10: [11],
    11: [],
    12: [],  # 7 is another possible destination
}


def dfs(current, target, path=None):

    if path is None:
        path = []

    path = path + [current]

    if current == target:
        print("found the path")
        print(f"the path is {path}")
        return

    for i in graph[current]:
        if i not in path:
            dfs(i, target, path)


dfs(1, 12)
