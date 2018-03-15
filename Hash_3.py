# encoding=utf-8
from struct import unpack_from
from hashlib import md5
from bisect import bisect_left

ORIGINAL_NUM_NODES = 100    # original node count
NEW_NUM_NODES = 101         # new node count
NUM_DATA = 100000

# hash function
def hash(data):
    data_md5 = md5(str(data)).digest()
    return unpack_from("=I", data_md5)[0]

# distribute data to different nodes
def distribute(original_nodes, new_nodes):
    transfer_count = 0
    for data in range(NUM_DATA):
        h = hash(data)
        original_index = bisect_left(original_nodes, h) % ORIGINAL_NUM_NODES
        new_index = bisect_left(new_nodes, h) % NEW_NUM_NODES
        if original_index != new_index:
            transfer_count += 1
    return transfer_count

if __name__ == '__main__':
    '''
        Case 3: 应用一致性Hash后, 需要移动的节点比例
    '''

    original_nodes = sorted([hash(i) for i in range(ORIGINAL_NUM_NODES)])   # 对node本身也取hash
    new_nodes = sorted([hash(i) for i in range(NEW_NUM_NODES)])             # 对node本身也取hash

    transfer_count = distribute(original_nodes, new_nodes)
    print("Percentage of data that need to be transferred: {}%".format(transfer_count * 100.0 / NUM_DATA))
