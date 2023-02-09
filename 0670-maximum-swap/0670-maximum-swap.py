class Solution:
    def maximumSwap(self, num: int) -> int:
        copy = list(str(num))
        ind = defaultdict(list)
        for i, x in enumerate(copy):
            ind[x].append(i)
        scopy = sorted(copy, reverse = True)
        for j, y in enumerate(scopy):
            if copy[j] == scopy[j]:
                continue
            else:
                copy[j], copy[ind[scopy[j]][-1]] = copy[ind[scopy[j]][-1]], copy[j]
                return int("".join(copy))
        return num