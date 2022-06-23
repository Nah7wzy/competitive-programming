class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # first sort according to the lastday.
        courses.sort(key=lambda x: x[1])
        totalDays = 0
        maxHeap = []
        
        for i in range(len(courses)):
            totalDays += courses[i][0]
            heappush(maxHeap, -courses[i][0])
            
            if courses[i][1] < totalDays:
                maxdur = heappop(maxHeap)
                totalDays += maxdur
       
        return len(maxHeap)