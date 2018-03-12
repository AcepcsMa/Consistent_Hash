# encoding=utf-8
from struct import unpack_from
from hashlib import md5
import matplotlib.pyplot as plt

NUM_NODES = 100
NUM_DATA = 100000
nodes = [0 for i in range(NUM_NODES)]

# hash function
def hash(data):
    data_md5 = md5(str(data)).digest()
    return unpack_from("=I", data_md5)[0]

# distribute data to different nodes
def distribute():
    for data in range(NUM_DATA):
        h = hash(data)
        index = h % NUM_NODES
        nodes[index] += 1

if __name__ == '__main__':
    '''
        Case 1: 正常情况下的数据分布
    '''

    distribute()
    max_node = max(nodes)
    min_node = min(nodes)
    print ("Node with max data: {0} piece of data".format(max_node))
    print ("Node with min data: {0} piece of data".format(min_node))

    # plot scatter graph
    x = [i for i in range(NUM_NODES)]
    y = nodes
    plt.scatter(x, y, c='r')
    plt.yticks(range(0, 2 * NUM_DATA / NUM_NODES, 100))
    plt.xlabel("Node Index")
    plt.ylabel("Data Count")
    plt.show()
