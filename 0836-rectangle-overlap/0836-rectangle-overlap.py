class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # Check if any of the rectangles have no area
        if (rec1[0] == rec1[2] or rec1[1] == rec1[3] or
                rec2[0] == rec2[2] or rec2[1] == rec2[3]):
            return False

        # Check if the rectangles overlap on the x-axis
        if rec1[2] <= rec2[0] or rec1[0] >= rec2[2]:
            return False

        # Check if the rectangles overlap on the y-axis
        if rec1[3] <= rec2[1] or rec1[1] >= rec2[3]:
            return False

        # If both x and y overlap, the rectangles overlap
        return True
