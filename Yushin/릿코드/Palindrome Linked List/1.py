class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        temp = []
        resultFirst = ListNode()
        resultFirst.val = -101
        if list1 == None and list2 == None:
            return None
        elif list1 != None and list2 == None:
            return list1
        elif list1 == None and list2 != None:
            return list2
        if list1.val > list2.val:
            result.val = list2.val
            list2 = list2.next
        else:
            result.val = list1.val
            list1 = list1.next
        result.next = resultFirst
        while list1 != None and list2 != None:
            if list1.val > list2.val:
                val = list2.val
                list2 = list2.next
            else:
                val = list1.val
                list1 = list1.next
            resultFirst.val = val
            if (list1 == None or list2 == None):
                break
            resultFirst.next = ListNode()
            resultFirst = resultFirst.next

        if list1 == None:
            if (resultFirst.val == -101):
                result.next = list2
            else:
                resultFirst.next = list2
        else:
            if (resultFirst.val == -101):
                result.next = list1
            else:
                resultFirst.next = list1

        return result
