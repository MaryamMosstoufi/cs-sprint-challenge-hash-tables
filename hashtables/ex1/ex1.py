def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    dic = {}
    for index in range(length):
        if weights[index] in dic:
            if weights[index] * 2 == limit:
                return(index, dic[weights[index]])
        else:
            dic[weights[index]] = index
    for key in dic:
        match = limit - key
        if match in dic:
            if dic[match] > dic[key]:
                return (dic[match], dic[key])
            else:
                return (dic[key], dic[match])
    # This solution was not using hashtables or dictionaries
    # if length < 2:
    #     return None
    # for i in range(0, length):
    #     for j in range(1, length):
    #         sum = weights[i] + weights[j]
    #         if sum == limit:
    #             if i >= j:
    #                 return (i, j)
    #             else:
    #                 return (j, i)
    return None


get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7)
