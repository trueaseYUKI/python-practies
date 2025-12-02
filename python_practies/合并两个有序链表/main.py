# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        # 数据区域
        self.val = val
        # 指针区域
        self.next = next

    def visit_link(self):
        temp = self
        while temp is not None:
            print(f"{temp.val}",end="，")
            temp = temp.next





def list_to_link(my_list:Optional[List[int]])->ListNode:
    head = ListNode()
    temp = head
    for index in range(0,len(my_list)):
        # 如果是第一个数据
        if index == 0:
            head.val = my_list[index]
        else:
            node = ListNode(my_list[index])
            temp.next = node
            temp = temp.next

    return head



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # 1.判断是否有空
        temp2 = list1
        cnt = 0
        while temp2 is not None:
            cnt += 1
            temp2 = temp2.next

        if cnt == 0:
            return list2

        temp2 = list2
        cnt = 0
        while temp2 is not None:
            cnt += 1
            temp2 = temp2.next

        # 2.判断二者是否有空
        if cnt == 0:
            return list1


        # 3.对两者进行遍历对比大小
        temp1 = list1
        temp2 = list2
        cnt = 0
        head = ListNode()
        temp = head

        # 4. 只要两个指针中的一个没有指向None
        while temp1 is not None or temp2 is not None:
            # 如果 temp1 和 temp2 都不是空
            if temp1 is not None and temp2 is not None:
                if temp1.val <= temp2.val:
                    if cnt == 0:
                        head.val = temp1.val
                        temp = head
                        cnt += 1
                    else:
                        node = ListNode(temp1.val)
                        temp.next = node
                        temp = temp.next
                    temp1 = temp1.next
                else:
                    if cnt == 0:
                        head.val = temp2.val
                        temp = head
                        cnt += 1
                    else:
                        node = ListNode(temp2.val)
                        temp.next = node
                        temp = temp.next
                    temp2 = temp2.next
            # 如果temp1 为空
            elif temp1 is None and temp2 is not None:
                node = ListNode(temp2.val)
                temp.next = node
                temp = temp.next
                temp2 = temp2.next
            # temp2为空
            elif temp1 is not None and temp2 is None:
                node = ListNode(temp1.val)
                temp.next = node
                temp = temp.next
                temp1 = temp1.next


        return head


def main():
    s = Solution()
    list1 = list_to_link([1,2,4])
    list2 = list_to_link([1,3,4])
    res = s.mergeTwoLists(list1,list2)
    print(res.visit_link())
    pass


if __name__ == '__main__':
    main()
    pass
