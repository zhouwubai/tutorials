class Node(object):
    def __init__(self, low=None, high=None):
        self.low = low
        self.high = high
        self.left = None
        self.right = None
        self.ints = []

    def isLeaf(self):
        return (not self.left and not self.right)


def inorder(root):
    if not root:
        return
    else:
        inorder(root.left)
        print("[%s, %s]" % (root.low, root.high))
        print("contains intervals: %s" % root.ints)
        inorder(root.right)


def makeTree(arr):
    n = len(arr)
    return makeTreeUtil(arr, 0, n - 1)


def makeTreeUtil(arr, start, end):
    '''arr is the sorted end points'''
    if start >= end:
        return Node(arr[start], arr[start])
    else:
        mid = (start + end) / 2
        root = Node(arr[start], arr[end])
        root.left = makeTreeUtil(arr, start, mid)
        root.right = makeTreeUtil(arr, mid + 1, end)
        return root


def insert(root, arr, idx):
    if not root or root.low > arr[idx][1] or root.high < arr[idx][0]:
        return

    if arr[idx][0] <= root.low and arr[idx][1] >= root.high:
        root.ints.append(idx)
    else:
        # corner condition will be check in the next loop
        insert(root.left, arr, idx)
        insert(root.right, arr, idx)


def searchOverlap(root, x):
    '''
    find the interval contains x
    '''
    res = []
    searchOverlapUtil(root, x, res)
    return res


def searchOverlapUtil(root, x, res):
    if not root or root.low > x or root.high < x:
        return
    else:
        if root.low <= x <= root.high:
            res.extend(root.ints)
        else:
            searchOverlapUtil(root.left, x, res)
            searchOverlapUtil(root.right, x, res)


if __name__ == '__main__':
    '''
    [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]
    '''
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12],
                 [15, 20, 10], [19, 24, 8]]
    n = len(buildings)
    starts, ends = [], []
    for i in range(n):
        starts.append(buildings[i][0])
        ends.append(buildings[i][1])
    ends = sorted(ends)

    i, j = 1, 0
    all_ends = [starts[0]]
    while i < n and j < n:
        if starts[i] < ends[j]:
            if starts[i] != all_ends[-1]:
                all_ends.append(starts[i])
            i += 1
        else:
            if ends[j] != all_ends[-1]:
                all_ends.append(ends[j])
            j += 1
    while i < n:
        if starts[i] != all_ends[-1]:
            all_ends.append(starts[i])
        i += 1
    while j < n:
        if ends[j] != all_ends[-1]:
            all_ends.append(ends[j])
        j += 1

    print(all_ends)

    root = makeTree(all_ends)
    # inorder(root)
    for i in range(n):
        insert(root, buildings, i)
    inorder(root)



