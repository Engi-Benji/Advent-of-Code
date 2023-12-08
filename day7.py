f = open("./inputs/day8.txt", "r")

movement = ""
nodes = []

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

        nodes.append(node)
    count += 1

currentLocations = []

for node in nodes:
    if node[0][-1] == "A":
        currentLocations.append(node[0])

count = 0
atDestination = False

while not atDestination:
    for direction in movement:
        destinations = []
        for currentLocation in currentLocations:
            moved = False
            for node in nodes:
                if node[0] == currentLocation and not moved:
                    if direction == "L":
                        destinations.append(node[1])
                    else:
                        destinations.append(node[2])
                    moved = True
                    break

        currentLocations = destinations
        count += 1
        allArrived = True

        for currentLocation in currentLocations:
            # print(currentLocation[-1])
            if not currentLocation[-1] == "Z":
                allArrived = False
                break

        #print(currentLocations)
        #print(count)

        if allArrived:
            atDestination = True
            break

        if count % 100000 == 0:
            print(count)

print(currentLocations)
print(count)