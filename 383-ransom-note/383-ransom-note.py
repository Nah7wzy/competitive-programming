class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc = collections.Counter(ransomNote)
        mc = collections.Counter(magazine)

        for i, j in rc.items():
            if i not in mc or mc[i] < j:
                return False

        return True