f = open("./inputs/day8.txt", "r")

movement = ""
nodes = {}

count = 0
for line in f.readlines():
    node = []
    if count == 0:
        movement = line.strip()
    elif count == 1:
        print("blank")
    else:
        line = line.replace(" ", "")
        line = line.replace("(", "")
        line = line.replace(")", "")

        initSplit = line.strip().split("=")
        node.append(initSplit[0])

        destspplit = initSplit[1].split(",")
        node.append(destspplit[0])
        node.append(destspplit[1])

        nodes[node[0]] = [node[1], node[2]]
    count += 1

currentLocations = [key for key, value in nodes.items() if 'A' in key[-1]]
print(currentLocations)

count = 0
atDestination = False

while not atDestination:
    for direction in movement:
        destinations = []
        for currentLocation in currentLocations:

            if direction == "L":
                destinations.append(nodes.get(currentLocation)[0])
            else:
                destinations.append(nodes.get(currentLocation)[1])

        currentLocations = destinations
        count += 1

        allArrived = True
        for currentLocation in currentLocations:
            # print(currentLocation[-1])
            if not currentLocation[-1] == "Z":
                allArrived = False
                break

        # print(currentLocations)
        # print(count)

        if allArrived:
            atDestination = True
            break

        if count % 1000000000 == 0:
            print(count)

print(currentLocations)
print(count)
