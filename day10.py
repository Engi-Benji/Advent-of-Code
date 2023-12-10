def travelPipe(pipes, location, entry):
    return 0


if __name__ == '__main__':
    # |
    # -
    # L
    # J
    # 7
    # .
    # S

    pipes = []
    f = open("inputs/day10.txt", "r")

    for line in f.readlines():
        pipes.append(line.strip())

    currentLocation = []
    for i in range(0, len(pipes)):
        for j in range(0, len(pipes[i])):
            if pipes[i][j] == "S":
                print(f"{i}\n{j}")
                currentLocation.append(i)
                currentLocation.append(j)

    start = False
    direction = "E"
    count = 0
    edges = []
    while not start:
        if direction == "E":
            currentLocation[1] += 1
        elif direction == "W":
            currentLocation[1] -= 1
        elif direction == "N":
            currentLocation[0] -= 1
        else:
            currentLocation[0] += 1

        edges.append([currentLocation[0], currentLocation[1]])
        location = pipes[currentLocation[0]][currentLocation[1]]

        if location == "S":
            start = True
        elif location == "-":
            if direction == "E":
                direction = "E"
            else:
                direction = "W"
        elif location == "7":
            if direction == "E":
                direction = "S"
            else:
                direction = "W"
        elif location == "J":
            if direction == "S":
                direction = "W"
            else:
                direction = "N"
        elif location == "|":
            if direction == "S":
                direction = "S"
            else:
                direction = "N"
        elif location == "L":
            if direction == "S":
                direction = "E"
            else:
                direction = "N"
        elif location == "F":
            if direction == "W":
                direction = "S"
            else:
                direction = "E"

        count += 1

print(count)

count = 0
i = 0
for pipe in pipes:
    j = 0
    for location in pipe:

        crosses = 0
        for y in range (j, len(pipe)):
            if [i, y] in edges and pipes[i][y] == "|":
                crosses += 1

        if crosses % 2 == 1:
            count += 1

        j += 1
    i += 1

print(count)
