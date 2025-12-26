from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # 求两个数的最大公约数
    def gcd(self, a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        is_add = False
        temp = None
        while p != None:
            # 如果当前值的下一个不等于 None，并且两个数中没有进行其他的添加
            if p.next != None and not is_add:
                # 求最大公约数
                temp = p.next
                cd = self.gcd(p.val,temp.val)
                # 插入最大公约数到两个数之间
                node = ListNode(val=cd)
                node.next = temp
                p.next = node
                # 将插入状态转为True
                is_add = True
            elif is_add:
                is_add = False

            p = p.next


        return head



def array_to_nodes(arr:List[int]):
    head = ListNode(val=arr[0])
    temp = head
    for i in range(1,len(arr)):
        node = ListNode(val=arr[i])
        temp.next = node
        temp = temp.next

    return head

def main():
    head = array_to_nodes([18,6,10,3])
    s = Solution()
    res = s.insertGreatestCommonDivisors(head)
    print(f"插入完最大公约数后的链表：{res}")

if __name__ == "__main__":
    main()