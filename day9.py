def findNextValue(sequence):
    diffs = []
    nextDiff = 0
    for i in range(0, len(sequence) - 1):
        diffs.append(sequence[i + 1] - sequence[i])

    allZero = True
    for diff in diffs:
        if not diff == 0:
            allZero = False

    if not allZero:
        nextDiff = findNextValue(diffs)
        return diffs[-1] + nextDiff
    else:
        return 0

def findPrevValue(sequence):
    diffs = []
    nextDiff = 0
    for i in range(0, len(sequence) - 1):
        diffs.append(sequence[i + 1] - sequence[i])

    allZero = True
    for diff in diffs:
        if not diff == 0:
            allZero = False

    if not allZero:
        nextDiff = findPrevValue(diffs)
        return diffs[0] - nextDiff
    else:
        return 0

if __name__ == '__main__':

    f = open("inputs/day9.txt", "r")
    count = 0

    # for line in f.readlines():
    #     sequence = []
    #     for num in line.strip().split(" "):
    #         sequence.append(int(num))
    #
    #     count += sequence[-1] + findNextValue(sequence)
    #
    # print(count)
    #

    for line in f.readlines():
        sequence = []
        for num in line.strip().split(" "):
            sequence.append(int(num))

        count += sequence[0] - findPrevValue(sequence)

    print(count)