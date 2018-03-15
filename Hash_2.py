# encoding=utf-8
from struct import unpack_from
from hashlib import md5

LESS_NUM_NODES = 99         # less nodes
ORIGINAL_NUM_NODES = 100    # original nodes
MORE_NUM_NODES = 101        # more nodes
NUM_DATA = 100000

# hash function
def hash(data):
    data_md5 = md5(str(data)).digest()
    return unpack_from("=I", data_md5)[0]

# distribute data to more nodes
def distribute_more():
    transfer_count = 0
    for data in range(NUM_DATA):
        h = hash(data)
        original_index = h % ORIGINAL_NUM_NODES
        more_index = h % MORE_NUM_NODES
        if original_index != more_index:
            transfer_count += 1
    return transfer_count

# distribute data to less nodes
def distribute_less():
    transfer_count = 0
    for data in range(NUM_DATA):
        h = hash(data)
        original_index = h % ORIGINAL_NUM_NODES
        less_index = h % LESS_NUM_NODES
        if original_index != less_index:
            transfer_count += 1
    return transfer_count

if __name__ == '__main__':
    '''
        Case 2: 当出现增/删节点时的数据分布情况
    '''

    # 新增节点
    transfer_count = distribute_more()
    print("##### When one new node is added #####")
    print("Data that need to be transferred: {}".format(transfer_count))
    print("Percentage of data that need to be transferred: {}%".format(transfer_count * 100.0 / NUM_DATA))

    # 删除节点
    transfer_count = distribute_less()
    print("\n##### When one old node is deleted #####")
    print("Data that need to be transferred: {}".format(transfer_count))
    print("Percentage of data that need to be transferred: {}%".format(transfer_count * 100.0 / NUM_DATA))
