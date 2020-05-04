def Find(target, array):
    if array == []:
        return False
    elif len(array[0]) == 0:
        return False

    else:
        col = len(array)
        row = len(array[0])
        for i in range(col):
            for j in range(row):
                if array[i][j] == target:
                    return True
        return False

array = [[1, 2, 4, 8], [3, 3, 7, 10]]
print(Find(5, array))