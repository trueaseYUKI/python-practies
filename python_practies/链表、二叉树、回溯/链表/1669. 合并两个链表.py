from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cnt = 0
        p1 = list1
        p2 = list2
        temp = None

        while p2.next != None:
            p2 = p2.next

        while p1 != None:

            # 如果当前指向要删除结点的前一个
            if cnt == a - 1:
                temp = p1

            if cnt == b:
                temp.next = list2
                p2.next = p1.next


            p1 = p1.next
            cnt += 1

        return list1


def array_to_nodes(arr:List[int]):
    head = ListNode(val=arr[0])
    temp = head
    for i in range(1,len(arr)):
        node = ListNode(val=arr[i])
        temp.next = node
        temp = temp.next

    return head

def main():
    list1 = array_to_nodes([10,1,13,6,9,5])
    list2 = array_to_nodes([1000000,1000001,1000002])
    s = Solution()
    res = s.mergeInBetween(list1,3,4,list2)
    print(f"链表结点变化之后：{res}")

if __name__ == "__main__":
    main()