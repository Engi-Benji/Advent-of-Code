def newApplyMap(seed, seedSoil):
    soil = 0
    unmapped = True

    count = 0
    offset = 0
    print(seed)
    while unmapped:
        map = seedSoil[count]

        if int(seed) < int(map[1]) and count == 0:
            soil = int(seed)
            unmapped = False
        elif int(map[1]) <= int(seed) < int(map[1]) + int(map[2]):
            soil = int(map[0]) + int(seed) - int(map[1])
            unmapped = False
        elif int(seed) >= int(map[1]) + int(map[2]):
            if map == seedSoil[-1]:
                soil = int(seed) - int(map[2]) - offset
                unmapped = False
            else:
                if int(seed) < int(seedSoil[count + 1][1]):
                    soil = int(map[0]) + int(seed) - int(map[2])
                    unmapped = False
                else:
                    offset = offset + int(seedSoil[count + 1][1]) - (int(map[1]) + int(map[2]))
        elif int(seed) < int(map[1]) and not count == 0:
            soil = int(seed) - int(map[2]) - offset
            unmapped = False

        print(f"{count} : {unmapped}")
        count += 1

    return soil


def sorter(ms):
    temp = []
    for x in ms:
        temp.append(x[1])

    sorted_array = [x for y, x in sorted(zip(temp, ms))]
    return sorted_array
