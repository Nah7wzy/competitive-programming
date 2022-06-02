class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)        
        heap = [-x  for x in count.values()]
        heapify(heap)
        time = 0
        
        if n == 0: return len(tasks)
        
        while len(heap) > 0:
            temp = n
            arr = []
            
            while temp >= 0:
                arr.append(heappop(heap)+1)
                time += 1
                temp -= 1
                
                if len(heap) == 0 and arr[0] != 0:
                    time += (temp+1)
                    break
                elif len(heap) == 0:
                    break

            for i in arr:
                if i == 0:
                    break
                else:
                    heappush(heap, i)
            
        return time
            
     