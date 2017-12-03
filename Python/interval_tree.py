class Interval(object):
    def __init__(self, low=0, high=0):
        self.low = low
        self.high = high

    @property
    def low(self):
        return self._low

    @low.setter
    def low(self, low):
        self._low = low

    @property
    def high(self):
        return self._high

    @high.setter
    def high(self, high):
        self._high = high

    def doOverlap(self, other):
        return (self.low <= other.high and other.low <= self.high)


class ITNode(object):
    def __init__(self, interval=None, left=None, right=None):
        self.interval = interval
        self.left = left
        self.right = right
        self.max = interval.high if interval else float('-inf')

    @classmethod
    def newNode(cls, interval):
        pass


def insert(root, interval):
    if not root:
        return ITNode(interval)

    r_low = root.interval.low
    if interval.low < r_low:
        root.left = insert(root.left, interval)
    else:
        root.right = insert(root.right, interval)

    # update max
    if root.max < interval.high:
        root.max = interval.high

    return root


def overlapSearch(root, interval):
    if not root:
        return None

    if root.interval.doOverlap(interval):
        return root.interval

    if root.left and root.left.max >= interval.low:
        return overlapSearch(root.left, interval)

    return overlapSearch(root.right, interval)


def inorder(root):
    if not root:
        return

    inorder(root.left)
    print('[%s, %s] max=%s' % (root.interval.low,
                               root.interval.high,
                               root.max))
    inorder(root.right)


if __name__ == "__main__":

    ints_arr = [[15, 20], [10, 30], [17, 19], [5, 20], [12, 15], [30, 40]]
    root = None
    for ints in ints_arr:
        root = insert(root, Interval(ints[0], ints[1]))

    print('Inorder traversal:\n')
    inorder(root)

    x = Interval(6, 7)
    print("Searching for interval [%s, %s]" % (x.low, x.high))
    res = overlapSearch(root, x)
    if res:
        print("Overlapping with [%s, %s]" % (res.low, res.high))
