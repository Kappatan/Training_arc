
class Solution:
    def reverseList(self, head) :
        prev=None
        cur=head
        while cur!=None:
            cur.next,prev,cur= prev,cur,cur.next
        return prev
