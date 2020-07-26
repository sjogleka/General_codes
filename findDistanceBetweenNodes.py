
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_distance_between_nodes_bst(nums, n1, n2):
    if not nums or n1 not in nums or n2 not in nums:
        return -1
    if n1 == n2:
        return 0
    parents = {}
    for num in nums:
        parents[num] = []
    root = TreeNode(nums[0])
    # construct BST
    for i in range(1, len(nums)):
        insert_node(root, nums[i], parents)
    # calculate distance
    parents_n1 = parents[n1]
    parents_n2 = parents[n2]
    l1 = len(parents_n1)
    l2 = len(parents_n2)

    if n1 in parents_n2:
        return l2 - parents_n2.index(n1)
    elif n2 in parents_n1:
        return l1 - parents_n1.index(n2)
    # find lowest common root
    else:
        idx = (l2 if l1 > l2 else l1) - 1

        while idx >= 0 and parents_n1[idx].val != parents_n2[idx].val:
            idx -= 1

        return (l1 - idx) + (l2 - idx)


def insert_node(root, val, parents):
    if not root:
        return TreeNode(val)

    parents[val].append(root)

    if root.val < val:
        root.right = insert_node(root.right, val, parents)
    else:
        root.left = insert_node(root.left, val, parents)

    return root


if __name__ == '__main__':
    #num = [5,6,3,1,2,4]
    num = [5, 6, 3, 1, 2, 4]
    #node1 = 2
    node1 = 1
    #node2 = 4
    node2 = 8

    print(get_distance_between_nodes_bst(num,node1,node2))