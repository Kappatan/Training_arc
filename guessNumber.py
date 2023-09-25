
class Solution11:
    def guessNumber(self, n: int, l=0) -> int:
        k= guess((l+n)//2)
        m=guess(1+(l+n)//2)
        if k==0:
            return (l+n)//2
        elif m==0:
            return 1+(l+n)//2
        elif k==-1:
            n=(l+n)//2
        elif k==1:
            l=(l+n)//2

        return self.guessNumber(n,l)