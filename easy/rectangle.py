"""
A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1)
are the coordinates of its bottom-left corner, and (x2, y2) are the
coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.
To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false

Both rectangles rec1 and rec2 are lists of 4 integers.
All coordinates in rectangles will be between -10^9 and 10^9.
"""
def overlap(coor1, coor2):
    # figure out the coordinates for the two remaining corners
    # at least one of the points needs to be in the range of the other rectangle
    


if __name__ == "__main__":
    rec1 = [0, 0, 2, 2]
    rec2 = [1, 1, 3, 3]

    overlap(rec1, rec2)