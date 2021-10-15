class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        for i in range(len(min(strs))):
            for ele in strs:
                if strs[0][i] != ele[i]:
                    return common_prefix
            common_prefix += ele[i]
        return common_prefix
