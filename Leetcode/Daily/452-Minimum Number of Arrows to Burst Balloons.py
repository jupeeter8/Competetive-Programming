from typing import List

# LC 452. Minimum Number of Arrows to burst balloons
# Given diameter of balloons (xstart, xend), find the number of minimum arrows
# required to pop all ballons

# Approach 1: Greeady: Sort the points based on the xend, this way the end
# of the diameterof the next balloon, provided x[i+1][0] < x[i][1]
# will always be x[i][1] <= x[i+1][1]

# This way all the next ballons that have the start point <= the previous
# decided end point can be burst by a single arrow
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points = sorted(points, key=lambda x: x[1])  # Sort points by xend
        arrow = 1  # Atleast one arrow is required

        preEndpoint = points[0][1]  # Previous end point for which all next
        # ballons can be burst

        for i in range(1, len(points)):
            if points[i][0] > preEndpoint:  # If start point of current ballon
                # is greater than the previous end point it can't be burst by
                # the same arrow

                arrow += 1  # Add new arrow
                preEndpoint = points[i][1]  # Update previous end point to be
                # the current
        return arrow


def main():

    sol = Solution()
    res = sol.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]])
    print(res)


main()
