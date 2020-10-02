# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []
    queries_dic = {}
    for query in queries:
        queries_dic[query] = query
    for file in files:
        if file[file.rfind('/') + 1:] in queries_dic:
            result.append(file)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
