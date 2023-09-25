
def lengthOfLongestSubstring( s: str):
     d=[]
     l=0
     for c in s:
         if c in d:
            if len(d)>l:
                l=len(d)
            d.clear()
            d.append(c)
         else:
             d.append(c)
     if len(d) > l:
         l = len(d)
     return l