class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_ind = {char:ind for ind, char in enumerate(s)}
        start = end = 0
        res = []
        for ind, char in enumerate(s):
            end = max(end,last_ind[char])
            if ind == end:
                res.append(end-start+1)
                start = ind+1
        return res 