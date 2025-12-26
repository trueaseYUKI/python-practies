from cmath import inf
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        # 如果链表为空
        node = Node(val=insertVal)
        if head == None:
            node.next = node
            return node

        # 如果链表只有一个元素
        if head.next == head:
            head.next = node
            node.next = head
            return head

        p = head
        while True:
            # 正常遍历
            if p.val <= insertVal <= p.next.val:
                node.next = p.next
                p.next = node
                break
            # 如果是局部最值
            if p.val > p.next.val:
                # 插入值是全局最大 或 全局最小，都插在断点处
                if insertVal >= p.val or insertVal <= p.next.val:
                    node.next = p.next
                    p.next = node
                    break
            # 如果遍历的了链表尾部
            if p.next == head:
                # 说明链表所有的元素都是一样的
                node.next = head.next
                head.next = node
                break
            p = p.next
        return head


def array_to_nodes(arr:List[int]):
    if len(arr) == 0:
        return None
    head = Node(val=arr[0])
    temp = head
    for i in range(1,len(arr) - 1):
        node = Node(val=arr[i])
        temp.next = node
        temp = temp.next

    node = Node(val=arr[len(arr)-1])
    temp.next = node
    node.next = head

    return head


def main():
    s = Solution()
    head = array_to_nodes([2,2,2,2])
    res = s.insert(head,3)
    print(f"插入后的链表：{res}")

if __name__ == "__main__":
    main()