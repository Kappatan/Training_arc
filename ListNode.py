class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)+' '+ str(self.next)
    def reverseList(self, head) :
        cur=head
        prev=None
        while cur!=None:
            a=cur.next
            b=prev
            c=cur
            prev=c
            cur.next=b
            cur=a
        return  prev
    def oddEvenList(self, head) :
        cur=head
        k=0
        if head is None or head.next is None:
            return head
        even=cur
        odd=cur.next
        cur=cur.next
        cur=cur.next
        even_head=even
        odd_head=odd
        even.next=None
        odd.next=None
        while cur!=None:
            if k%2==0:
                even.next=cur
                even=even.next
                cur=cur.next
                even.next=None
                k+=1
            else:
                odd.next=cur
                odd=odd.next
                cur=cur.next
                odd.next=None
                k+=1
        even.next=odd_head
        return even_head
    def deleteMiddle(self, head):
        if not head.next:
            return None
        slow=head
        fast=head.next.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        slow.next=slow.next.next
        return head
    def clone_linked_list(self,head):
        if not head:
            return None

        clone_list = LinkedList()
        current_original = head

        while current_original:
            clone_list.append(current_original.val)
            current_original = current_original.next

        return clone_list
    def pairSum(self, head):
        slow,fast=head,head
        prev=None
        while fast and fast.next:
            fast=fast.next.next
            tmp=slow.next
            slow.next=prev
            prev=slow
            slow=tmp
        res=0
        while slow:
            res=max(res, prev.val+slow.val)
            prev=prev.next
            slow=slow.next
        return res