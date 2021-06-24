def get_all_directories(path):
    import os
    res = []
    path = os.path.abspath(path)
    print(path)

    def get_directories(path):

        for child in os.listdir(path):
            child_path = os.path.join(path, child)
            if os.path.isdir(child_path):
                get_directories(child_path)
            else:
                res.append(child_path)

    get_directories(path)
    print(res)


# bfs
def get_all_directories_by_queue(path):
    # 广度优先
    import os
    root = path
    queue = [root]
    res = []

    while len(queue):

        node = queue.pop(0)
        node = os.path.abspath(node)
        for child in os.listdir(node):
            child_path = os.path.join(node, child)
            if os.path.isdir(child_path):
                queue.append(child_path)
            else:
                res.append(
                    child_path
                )
    print(res)
    return res


if __name__ == '__main__':
    get_all_directories_by_queue('../')
    # get_all_directories('../')
