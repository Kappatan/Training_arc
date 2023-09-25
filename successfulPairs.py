
Loyar
Loyar
Sep 25, 2023 15 :43

Details
Solution
Python
Runtime
1371 ms
Beats
50.7 7%
Memory
37 MB
Beats
74.6 1%
Click the distribution chart to view more details
Related Tags
Select tags 0/ 5


class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        res = []

        def binarysearch(spell):
            (l, r) = (0, len(potions) - 1)
            while l <= r:
                mid = (l + r) // 2
                prod = spell * potions[mid]
                if prod >= success:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        for spell in spells:
            idx = binarysearch(spell)
            res.append(len(potions) - idx)
        return res
