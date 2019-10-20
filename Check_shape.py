import numpy as np

def check_shape(shape):

    shape_id = 0
    #list of all shape and their basic coordinates + id, sorted in likelihood of being placed
    all_shapes = {
        2: [[0, 0], [1, 0], [2, 0], [3, 0]],
        3: [[0, 0], [0, 1], [0, 2], [0, 3]],
        4: [[0, 0], [1, 0], [2, 0], [2, 1]],
        6: [[0, 0], [0, 1], [1, 1], [2, 1]],
        9: [[0, 0], [0, 1], [0, 2], [1, 2]],
        10: [[0, 0], [0, 1], [1, 0], [2, 0]],
        12: [[0, 0], [1, 0], [1, 1], [2, 0]],
        15: [[0, 0], [0, 1], [0, 2], [1, 1]],
        17: [[0, 0], [1, 0], [1, 1], [2, 1]],
        18: [[0, 0], [0, 1], [1, 1], [1, 2]],
        1: [[0, 0], [0, 1], [1, 0], [1, 1]],
        5: [[0, 0], [1, -2], [1, -1], [1, 0]],
        7: [[0, 0], [0, 1], [0, 2], [1, 0]],
        8: [[0, 0], [1, 0], [2, -1], [2, 0]],
        11: [[0, 0], [1, 0], [1, 1], [1, 2]],
        13: [[0, 0], [1, -1], [1, 0], [1, 1]],
        14: [[0, 0], [1, -1], [1, 0], [2, 0]],
        16: [[0, 0], [0, 1], [1, -1], [1, 0]],
        19: [[0, 0], [1, -1], [1, 0], [2, -1]]
    }

    shape.sort(key=lambda row: row[1]) #sort the imported list of coordinates by j value
    shape.sort(key=lambda row: row[0]) #sort the imported list of coordinates by i value
    i0 = shape[0][0] #change the imported list of ccordinates into the basic coordinates for comparison
    j0 = shape[0][1]
    for point in shape:
        point[0] = point[0] - i0
        point[1] = point[1] - j0
    #print(shape)
    for shp in all_shapes: #loop through the dictionary and find the correct shape id
        if np.array_equal(shape,all_shapes[shp]):
            shape_id = shp
            break

    return shape_id
