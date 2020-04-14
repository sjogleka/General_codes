# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        def mergeTwo(l1,l2):
            dummyNode = head = ListNode(0)
            while l1 and l2:
                if l1.val>l2.val:
                    dummyNode.next = l2
                    l2 =l2.next
                else:
                    dummyNode.next = l1
                    l1 = l1.next
                dummyNode = dummyNode.next

            if l1:
                dummyNode.next = l1
            elif l2:
                dummyNode.next = l2
            return head.next
        if len(lists)==0:
            return 0
        while len(lists)>1:
            l1 = lists.pop(0)
            l2 = lists.pop(0)
            lists.append(mergeTwo(l1,l2))

        return lists[0]












        '''
        temp = []
        for i in range(len(lists)):
            l1 = lists[i]
            while l1:
                temp.append(l1.val)
                l1 = l1.next

        temp.sort()

        dummyNode = head = ListNode(0)

        for i in range(len(temp)):
            dummyNode.next = ListNode(temp[i])
            dummyNode = dummyNode.next

        return head.next
        '''



