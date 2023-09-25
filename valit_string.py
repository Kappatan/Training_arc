
class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                l.append(i)
            elif l==[]:
                return False
            elif i==')':
                if l[-1]=='(':
                    l.pop()
                else:
                    return False
            elif i=='}':
                if l[-1]=='{':
                    l.pop()
                else:
                    return False
            elif i==']':
                if l[-1]=='[':
                    l.pop()
                else:
                    return False
        if l==[]:
            return True
        else:
            return False
