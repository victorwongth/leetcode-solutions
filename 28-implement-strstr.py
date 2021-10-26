class naiveSolution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        for i in range(len(haystack) - length + 1):
            if haystack[i:i+length] == needle:
                return i
        return -1
        
        
class kmpSoluton:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        
        lps = [0]
        prefix = 0
        i = 1
        while i < len(needle):
            if needle[i] == needle[prefix]:
                prefix += 1
                lps.append(prefix)
                i += 1
            else:
                if prefix == 0:
                    lps.append(prefix)
                    i += 1
                else:
                    prefix = lps[prefix - 1]  
        
        evaluated = []
        lps_index = 0            
        j = 0
        while j < len(haystack):
            if haystack[j] == needle[lps_index]:
                j += 1
                lps_index += 1
            else:
                if lps_index != 0:
                    lps_index = lps[lps_index - 1]
                else:
                    j += 1
            if lps_index == len(needle):
                return j - len(needle)
            
        return -1
