# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    swaps = []
    for i in range(int(len(data) / 2), -1, -1):
        shift_down(i, data, swaps)
    return swaps


def left_child(i) -> int:
    return (2 * i) + 1


def right_child(i) -> int:
    return (2 * i) + 2


def shift_down(i, data, swaps):
    minIndex = i
    l = left_child(i)
    if l < len(data) and data[l] < data[minIndex]:
        minIndex = l
    r = right_child(i)
    if r < len(data) and data[r] < data[minIndex]:
        minIndex = r
    if i != minIndex:
        data[i], data[minIndex] = data[minIndex], data[i]
        swaps.append((i, minIndex))
        shift_down(minIndex, data, swaps)


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
