class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(segment):
            return 0 <= int(segment) <= 255 and str(int(segment)) == segment

        def backtrack(s, segments, start, res):
            if start == len(s) and len(segments) == 4:
                res.append(".".join(segments))
                return
            if start >= len(s) or len(segments) >= 4:
                return
            for end in range(start, min(start + 3, len(s))):
                if is_valid(s[start:end + 1]):
                    backtrack(s, segments + [s[start:end + 1]], end + 1, res)

        res = []
        backtrack(s, [], 0, res)
        return res