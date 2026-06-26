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


#                possible("13204")
#                /               \
#        st[1:] /                 \ st[2:]
#              /                   \
#      possible("3204")         [Cache Hit!] possible("204") ──> Returns 1
#        /               \                   (Instantly skips decoding)
# st[1:] /                 \ st[2:]
#       /                   \
# possible("204")        (int("32") > 26) ──> Invalid path, branch blocked
#   /         \
#  / st[1:]    \ st[2:]
# /             \
# possible("04")  possible("4")
#   │               │
#   ▼               ▼
# (Starts with '0') st[1:] ──> possible("") ──> Returns 1
# Returns 0                     (Valid end of string)
