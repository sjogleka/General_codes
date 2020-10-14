'''
def LCA(root,ele1,ele2):

    if ele2>ele1:
        ele2,ele1 = ele1,ele2

    if root:
        return

    if ele1<root.val and ele2>root.val:
        return root

    return traverse(root,ele1,ele2)


def traverse(root,ele1, ele2):
    if ele1<root.val and ele2>root.val:
        return root

    if root.right and ele1>root.val and ele2>root.val:
        return traverse(root.right,ele1,ele2)
    elif root.left and ele1<root.val and ele2<root.val:
        return traverse(root.left,ele1,ele2)
'''


def checkCyclic(head):
    if not head:
        return False

    tempHead = head
    visited = set()

    while tempHead:
        if tempHead in visited:
            return True

        visited.add(tempHead)

        tempHead= tempHead.next

    return False

#3->2->4->2->6->4




















