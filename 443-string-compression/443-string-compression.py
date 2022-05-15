class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ''
        p1, p2 = 0, 0
        if len(chars)==1:
            pass
        else:
            while p2 < len(chars)-1:
                p2 = p2+1
                count = p2-p1

                if chars[p2] == chars[p1] and p2 != len(chars)-1:
                    continue

                elif chars[p2] == chars[p1] and p2 == len(chars)-1:
                    s += chars[p1]
                    s += str(count+1)
                else:
                    if p2-p1 == 1:
                        s += chars[p1]
                        if p2 == len(chars)-1:
                            s += chars[p2]
                    else:

                        s += chars[p1]
                        s += str(count)            
                        if p2 == len(chars)-1:
                            print(chars[p2])
                            s += chars[p2]
                    p1 = p2

            for i, j in enumerate(s):            
                chars[i] = j

            chars = chars[:len(s)]
        return len(chars)
        