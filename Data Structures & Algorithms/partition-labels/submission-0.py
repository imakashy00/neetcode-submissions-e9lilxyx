class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        i = 0
        res = []
        while i < len(s):
            last_ind_i = s.rfind(s[i])
            j = i+1
            count = 0
            while j < last_ind_i+1:
                last_ind_j = s.rfind(s[j])
                if last_ind_j > last_ind_i:
                    last_ind_i=last_ind_j
                j+=1
                count+=1
            res.append(count+1)
            i = last_ind_i+1
        return res
