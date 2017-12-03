class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class SEGNode(object):
    def __init__(self, interval=None, sum=0):
        self.interval = interval
        self.sum = sum
        self.left = None
        self.right = None


def makeSegTree(arr):
    n = len(arr)
    return makeSegTreeUtil(arr, 0, n - 1)


# we do no validate parameters
def makeSegTreeUtil(arr, start, end):
    if start >= end:
        return SEGNode(Interval(start, start), arr[start])
    else:
        mid = (start + end) / 2
        root = SEGNode(Interval(start, end))
        root.left = makeSegTreeUtil(arr, start, mid)
        root.right = makeSegTreeUtil(arr, mid + 1, end)
        root.sum = root.left.sum + root.right.sum
        return root


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print('sum[%s, %s]==%s' % (root.interval.start,
                               root.interval.end,
                               root.sum))
    inorder(root.right)


# do not validate parameters
def getSum(root, start, end):
    if start <= root.interval.start and end >= root.interval.end:
        return root.sum

    if start > root.interval.end or end < root.interval.start:
        return 0

    # be careful here
    mid = (root.interval.start + root.interval.end) / 2
    if mid < start:
        return getSum(root.right, start, end)
    elif mid > end:
        return getSum(root.left, start, end)
    else:
        return getSum(root.left, start, mid) + getSum(root.right, mid + 1, end)


# return diff after change
def update(root, idx, new_val):
    if idx < root.interval.start or idx > root.interval.end:
        return 0
    if idx == root.interval.start == root.interval.end:
        diff = new_val - root.sum
        root.sum = new_val
        return diff
    left_diff = update(root.left, idx, new_val)
    right_diff = update(root.right, idx, new_val)
    root.sum += left_diff + right_diff
    return left_diff + right_diff


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 11]
    segTree = makeSegTree(arr)
    # inorder(segTree)
    print(getSum(segTree, 1, 3))
    update(segTree, 1, 10)
    print(getSum(segTree, 1, 3))
