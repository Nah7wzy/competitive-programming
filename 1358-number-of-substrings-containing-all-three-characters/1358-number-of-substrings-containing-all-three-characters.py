class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        letters = set()
        count = defaultdict(int)
        i = j = 0
        res = 0
        while j < n:
            letters.add(s[j])
            count[s[j]] += 1
            while len(letters) == 3:
                res += (n - j)
                count[s[i]] -= 1
                if count[s[i]] == 0:
                    letters.remove(s[i])
                i += 1
            j += 1
        return res