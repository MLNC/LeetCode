class Solution(object):
    def longestCommonPrefixZip(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)

    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        result = strs[0]
        for curr in strs:
            while curr[:len(result)] != result:
                result = result[:-1]
                if not result:
                    return ""
        return result