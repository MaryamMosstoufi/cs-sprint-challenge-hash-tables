def intersection(arrays):
    """
    YOUR CODE HERE
    """
    dic = {}
    result = []
    for index in range(len(arrays)):
        for item in arrays[index]:
            if item in dic:
                dic[item].append(index)
            else:
                dic[item] = [index]
    for item in dic:
        if len(dic[item]) == len(arrays):
            result.append(item)
    # this solution took too long
    # for i in arrays[0]:
    #     searching = True
    #     while searching:
    #         for j in range(1, len(arrays)):
    #             if i not in arrays[j]:
    #                 searching = False
    #         result.append(i)
    #         searching = False
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
