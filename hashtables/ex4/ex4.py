def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    dic = {}
    result = []
    for i in a:
        dic[i] = i * -1
    for key in dic:
        if dic[key] in dic and key > 0:
            result.append(key)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
