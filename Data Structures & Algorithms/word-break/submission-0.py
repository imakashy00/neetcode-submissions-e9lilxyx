class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) # one for begining
        dp[0] = True # base Case
        word_set = set(wordDict) # converting to set for fast lookup O(1)
        max_len = max(len(word) for word in word_set)

        for i in range(1, len(s)+1):
            st_ind = max(0, i - max_len)
            for j in range(st_ind, i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]