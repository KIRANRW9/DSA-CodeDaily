class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range(len(str[0])):
          ch=str[0][i]
          for s in range(str[1:]:
            if i>len(s) or s[i]!=ch:
              return str[0][:i]
        return str[0]
