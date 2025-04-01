class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def swappairs(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    curr = head

    while curr and curr.next:
        first = curr
        second = curr.next

        prev.next = second
        first.next = second.next
        second.next = first

        prev = first
        curr = first.next
    
    return dummy.next

def printL(head):
    while head:
        print(head.val,end="->")
        head = head.next
    print("None")

head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))

new_head = swappairs(head)
printL(new_head)