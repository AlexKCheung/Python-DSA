def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
    x, y = 0, 0
    d = 0
    # NESW
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    output = 0
    # time limit exceeded if we don't use a hashmap for O(1) lookup 
    obstacles = {tuple(a) for a in obstacles}

    for command in commands:
        if command == -2:
            d = (d - 1) % 4
        elif command == -1:
            d = (d + 1) % 4
        else:
            dx, dy = direction[d]
            for i in range(command):
                if (x + dx, y + dy) in obstacles:
                    break
                x += dx
                y += dy
        output = max(output, x*x + y * y)
    return output
