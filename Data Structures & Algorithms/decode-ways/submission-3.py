class Solution:
    def numDecodings(self, s: str) -> int:
        hmap = {}
        def possible(st):
            if st == "":
                return 1
            if st[0] == '0' :
                return 0
            if st in hmap:
                return hmap[st]
            res =  possible(st[1:])
            if len(st) > 1 and int(st[:2]) <= 26:
                res += possible(st[2:])
            hmap[st] = res
            return res
        return possible(s)
 