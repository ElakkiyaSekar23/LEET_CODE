class Solution:
    def longestCommonPrefix(self, str) -> str:
        prefix=str[0]
        for w in str:
            while not w.startswith(prefix):
                prefix=prefix[:-1]
        return prefix