def saddle_points(matrix):
    if not matrix:
        return []
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")
    row_maxes = [max(row) for row in matrix]
    col_mins = [min(col) for col in zip(*matrix)]
    points = []
    for r, row in enumerate(matrix):
        for c, value in enumerate(row):
            if value == row_maxes[r] and value == col_mins[c]:
                points.append({"row": r + 1, "column": c + 1})
    return points
