# The square is 17.5 x 17.5cm (interior).

# There are 16 piece intersections in the standard solution (i.e., the
# one Arthur fabricated it with).

# Clearing denominators, the most efficient way to represent the
# geometry of the standard solution is in abstract units of 1/12 of
# the side length.
# - Conjecture: Are all vertices of all solutions confined to the
#   corresponding 13x13 grid?

points = {
    "Bottom left corner":  [0, 0],
    "Bottom right corner": [12, 0],
    "Top left corner":     [0, 12],
    "Top right corner":    [12, 12],
    "Bottom center edge":  [6, 0],
    "Left center edge":    [0, 6],
    "Top center edge":     [6, 12],
    "Center":              [6, 6],
    "Bottom half-right edge": [9, 0], # measured 13.1cm, but 3/4 seems more plausible
    # The left upper edge point seems colinear with the lower right
    # corner and the center left internal point.  It also seems to be
    # on a level with the 2/3, 2/3 point.  Both suggest it is at 0,
    # 2/3.
    "Left upper edge":     [0, 8],
    "Center half-left":    [3, 6], # Intersection of left half-diagonals
    "Center half-right":   [9, 6], # Intersection of right half-diagonals
    # Lower left is the intersection of the main diagonal with an
    # opposing half-diagonal, which means it would be at 1/3, 1/3
    "Lower left":          [4, 4],
    # There is a symmetric point on the other side
    "Upper right":         [8, 8],
    # There is a point that appears colinear with the bottom right
    # edge and the top right corner, as well as the bottom right
    # corner and the top center edge.  This makes it
    "Lower right":         [10, 4],
    # The last point seems to be directly above this one, and on the
    # main diagonal, which makes it
    "Extreme upper right": [10, 10]
}

# Each piece is coded counter-clockwise
pieces = [
    [points["Bottom left corner"],
     points["Bottom center edge"],
     points["Lower left"]],
    [points["Bottom left corner"],
     points["Lower left"],
     points["Center half-left"]],
    [points["Bottom left corner"],
     points["Center half-left"],
     points["Left center edge"]],
    [points["Left center edge"],
     points["Center half-left"],
     points["Left upper edge"]],
    [points["Top left corner"],
     points["Left upper edge"],
     points["Center half-left"],
     points["Top center edge"]],
    [points["Top center edge"],
     points["Center half-left"],
     points["Lower left"],
     points["Center"]],
    [points["Center"],
     points["Lower left"],
     points["Bottom center edge"]],
    [points["Bottom center edge"],
     points["Bottom half-right edge"],
     points["Center half-right"],
     points["Upper right"],
     points["Center"]],
    [points["Center"],
     points["Upper right"],
     points["Top center edge"]],
    [points["Top center edge"],
     points["Upper right"],
     points["Top right corner"]],
    [points["Top right corner"],
     points["Extreme upper right"],
     points["Bottom right corner"]],
    [points["Bottom right corner"],
     points["Extreme upper right"],
     points["Upper right"]],
    [points["Center half-right"],
     points["Bottom half-right edge"],
     points["Lower right"]],
    [points["Lower right"],
     points["Bottom half-right edge"],
     points["Bottom right corner"]]
]

# TODO
# - Render the pieces in this configuration to check that I coded the
#   puzzle right (and to debug rendering).
# - Do I want to somehow check that I coded the pieces in
#   counter-clockwise order?  e.g., by rendering them with arrows?
# - Code the puzzle in z3 and check that the standard solution is a
#   solution, and that extraction works.
#   - Maybe incrementally add constraints:
#     - Containment in the field
#     - Non-overlap of pieces
# - Code a model search loop that finds all the solutions.
#   - How, exactly?
