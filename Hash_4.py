# encoding=utf-8
from struct import unpack_from
from hashlib import md5
from bisect import bisect_left
import matplotlib.pyplot as plt

NUM_NODES = 100    # original node count
NUM_DATA = 100000

# hash function
def hash(data):
    data_md5 = md5(str(data)).digest()
    return unpack_from("=I", data_md5)[0]

# distribute data to different nodes
def distribute(nodes, stat):
    for data in range(NUM_DATA):
        h = hash(data)
        index = bisect_left(nodes, h) % NUM_NODES
        stat[index] += 1


if __name__ == '__main__':
    '''
        Case 4: 应用一致性Hash后, 数据的分布情况
    '''

    nodes = sorted([hash(i) for i in range(NUM_NODES)])
    stat = [0 for i in range(NUM_NODES)]

    distribute(nodes, stat)
    max = max(stat)
    min = min(stat)
    print("Node with max data: {} piece of data".format(max))
    print("Node with min data: {} piece of data".format(min))

    # plot scatter graph
    x = [i for i in range(NUM_NODES)]
    y = stat
    plt.scatter(x, y, c='r')
    plt.yticks(range(0, 10 * NUM_DATA / NUM_NODES, 1000))
    plt.xlabel("Node Index")
    plt.ylabel("Data Count")
    plt.show()

