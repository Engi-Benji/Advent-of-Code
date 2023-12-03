def leftValue(lineCharList, char):
    value = []
    count = 0
    for point in lineCharList[char[1]]:
        if "." in point and count < char[2]:
            value = []
        elif not "." in point and count < char[2]:
            value.append(point)
        count += 1

    return "".join(value)


def rightValue(lineCharList, char):
    value = []
    count = len(lineCharList[char[1]])

    for point in lineCharList[char[1]][::-1]:
        if "." in point and count > char[2]:
            value = []
        elif not "." in point and count > char[2]:
            value.append(point)
        count -= 1

    temp = []
    for dig in value:
        if dig.isdigit():
            temp.append(dig)

    value = reversed(temp)

    return "".join(value)


if __name__ == '__main__':
    f = open("./inputs/day3.txt", "r")

    lineList = f.readlines()
    lineCharList = []
    charLocation = []

    for line in lineList:
        charList = []
        for char in line:
            charList.append(char)
        lineCharList.append(charList)


    i = 0
    for line in lineCharList:
        j = 0
        for char in line:
            if not char.isdigit() and not "." in char and not "\n" in char:
                charLocation.append([char, i, j])
            j += 1
        i += 1

    # print(charLocation)
    ratios = []

    for char in charLocation:
        numbers = []
        bottom = [lineCharList[char[1] + 1][char[2] - 1], lineCharList[char[1] + 1][char[2]],
                  lineCharList[char[1] + 1][char[2] + 1]]
        left = [lineCharList[char[1]][char[2] - 1]]
        right = [lineCharList[char[1]][char[2] + 1]]
        top = [lineCharList[char[1] - 1][char[2] - 1], lineCharList[char[1] - 1][char[2]],
               lineCharList[char[1] - 1][char[2] + 1]]

        if "*" in char[0]:
            if left[0].isdigit():
                numbers.append(leftValue(lineCharList, char))
                if not leftValue(lineCharList, char).isdigit():
                    print(leftValue(lineCharList, char))

            if right[0].isdigit():
                numbers.append(rightValue(lineCharList, char))
                if not rightValue(lineCharList, char).isdigit():
                    print(rightValue(lineCharList, char))

            if bottom[0].isdigit() and bottom[1].isdigit() and bottom[2].isdigit():
                numbers.append("".join(bottom))
                if not "".join(bottom).isdigit():
                    print("".join(bottom))

            elif bottom[0].isdigit() and bottom[1].isdigit() and not bottom[2].isdigit():
                numbers.append(leftValue(lineCharList, [char[0], (char[1] + 1), char[2]+1]))

                if not leftValue(lineCharList, [char[0], (char[1] + 1), char[2]]).isdigit():
                    print(leftValue(lineCharList, [char[0], (char[1] + 1), char[2]]))

            elif bottom[0].isdigit() and not bottom[1].isdigit() and bottom[2].isdigit():
                numbers.append(leftValue(lineCharList, [char[0], char[1] + 1, char[2]]))
                numbers.append(rightValue(lineCharList, [char[0], char[1] + 1, char[2]+1]))
            elif bottom[0].isdigit() and not bottom[1].isdigit() and not bottom[2].isdigit():
                numbers.append(leftValue(lineCharList, [char[0], char[1] + 1, char[2]]))
            elif not bottom[0].isdigit() and bottom[1].isdigit() and bottom[2].isdigit():
                numbers.append(rightValue(lineCharList, [char[0], char[1] + 1, char[2]]))
            elif not bottom[0].isdigit() and bottom[1].isdigit() and not bottom[2].isdigit():
                numbers.append("".join(bottom[1]))
            elif not bottom[0].isdigit() and not bottom[1].isdigit() and bottom[2].isdigit():
                numbers.append(rightValue(lineCharList, [char[0], char[1] + 1, char[2]+1]))
            elif not bottom[0].isdigit() and not bottom[1].isdigit() and not bottom[2].isdigit():
                i = 0

            if top[0].isdigit() and top[1].isdigit() and top[2].isdigit():
                numbers.append("".join(top))
            elif top[0].isdigit() and top[1].isdigit() and not top[2].isdigit():
                numbers.append(leftValue(lineCharList, [char[0], char[1] - 1, char[2]+1]))
            elif top[0].isdigit() and not top[1].isdigit() and top[2].isdigit():
                numbers.append(leftValue(lineCharList, [char[0], char[1] - 1, char[2]]))
                numbers.append(rightValue(lineCharList, [char[0], char[1] - 1, char[2]+1]))
            elif top[0].isdigit() and not top[1].isdigit() and not top[2].isdigit():
                numbers.append(leftValue(lineCharList, [char[0], char[1] - 1, char[2]]))
            elif not top[0].isdigit() and top[1].isdigit() and top[2].isdigit():
                numbers.append(rightValue(lineCharList, [char[0], char[1] - 1, char[2]]))
            elif not top[0].isdigit() and top[1].isdigit() and not top[2].isdigit():
                numbers.append("".join(top[1]))
            elif not top[0].isdigit() and not top[1].isdigit() and top[2].isdigit():
                numbers.append(rightValue(lineCharList, [char[0], char[1] - 1, char[2]+1]))
            elif not top[0].isdigit() and not top[1].isdigit() and not top[2].isdigit():
                i = 0

            if len(numbers) > 1:
                temp = 1
                for num in numbers:
                    temp = temp * int(num)

                ratios.append(temp)
intArr = []
print(ratios)
count = 0
for num in ratios:
    try:
        intArr.append(int(num))
    except:
        print(f"{num} + {count}")
    count += 1
print(sum(intArr))
