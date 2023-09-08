class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        max_lines = 0

        # get best straight line for each point
        for i in range(len(points)):
            slopes = {0:0}

            # The best straight line is the maximum number of repeated slopes of all points relative to this point.
            for j in range(i+1, len(points)):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]

                if x1 == x2 : # handling division by zero (slope = infinity)
                    try:
                        slope = 'inf'
                        slopes[slope] += 1
                    except: # save slope
                        slopes[slope] = 1
                else:
                    try:
                        slope = (y2-y1)/(x2-x1) # get slope
                        slopes[slope] += 1
                    except: # save slope
                        slopes[slope] = 1
            max_lines = max(slopes.values()) if max(slopes.values()) > max_lines else max_lines

        return (max_lines+1)

# to visualize points
# import matplotlib.pyplot as plt
# plt.scatter([p[0] for p in points], [p[1] for p in points])
# plt.show()