from Place_Shape import place
from Find_neighbour import find_neighbour

def brute_place(D, T, S, shape, cou):
    y_len = len(D)
    x_len = len(D[0])

    #print("using brute")
    for point in shape: #mark the imported nodes as placed
        neighbour = find_neighbour(D, shape, point[0], point[1], [])
        for points in neighbour:
            D[points[0]][points[1]] = D[points[0]][points[1]] - 1
        T[point[0]][point[1]] = 0
        D[point[0]][point[1]] = float('inf')
        #print("brute used")
    if len(shape) > 2: #if there are more than 2 neighbouring nodes to be brute placed, it is worth it
        for point in shape: #find possible neighbours that is not in the target but valid to be placed
            if point[0] + 1 < y_len and [point[0] + 1, point[1]] not in shape:
                if D[point[0] + 1][point[1]] == float('inf') and S[point[0] + 1][point[1]] == (0, 0):
                    shape.append([point[0] + 1, point[1]])
            if len(shape) == 4: break
            if point[1] + 1 < x_len and [point[0], point[1] + 1] not in shape:
                if D[point[0]][point[1] + 1] == float('inf') and S[point[0]][point[1] + 1] == (0, 0):
                    shape.append([point[0], point[1] + 1])
            if len(shape) == 4: break
            if point[0] - 1 >= 0 and [point[0] - 1, point[1]] not in shape:
                if D[point[0] - 1][point[1]] == float('inf') and S[point[0] - 1][point[1]] == (0, 0):
                    shape.append([point[0] - 1, point[1]])
            if len(shape) == 4: break
            if point[1] - 1 >= 0 and [point[0], point[1]-1] not in shape:
                if D[point[0]][point[1] - 1] == float('inf') and S[point[0]][point[1] - 1] == (0, 0):
                    shape.append([point[0], point[1] - 1])
            if len(shape) == 4: break
        #print(shape)
        if len(shape) == 4: #if the generated shape has four nodes, place it with the palce function
            D, T, S, cou = place(D, T, S, shape, cou)
            #print("brute shape placed")
            #print("brute used")
        else: #if it doesnt have a length of 4, it is impossible to brute place at that node, just mark them as placed
            for point in shape:
                T[point[0]][point[1]] = 0
                D[point[0]][point[1]] = float('inf')
            #print("brute shape removed")
            #print("brute used")


    return D, T, S, cou


