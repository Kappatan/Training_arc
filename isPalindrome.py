class Solution:
    def isPalindrome(self, xx: int) :
        if xx<0 :
            return False
        else:
            xxx=str(xx)
            for i in range (len(xxx)):
                if xxx[i]!=xxx[len(xxx)-i-1]:
                    return False
            return True