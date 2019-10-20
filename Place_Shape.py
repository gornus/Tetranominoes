from Check_shape import check_shape
from copy import deepcopy
from Find_neighbour import find_neighbour

def place(D, T, S, shape, cou):
    #print("placing shape")
    ID = check_shape(deepcopy(shape)) #find the shape id
    for point in shape: #place the shape for each node
        #print(shape)
        #print(point)
        T[point[0]][point[1]] = 0
        D[point[0]][point[1]] = float('inf')
        neighbour = find_neighbour(D,shape,point[0],point[1],[])
        for points in neighbour: #update the degree matrix
            D[points[0]][points[1]] = D[points[0]][points[1]] - 1
        S[point[0]][point[1]] = (ID,cou)
        #print((ID,cou))
    #print("shape number %d placed" % (cou))
    cou = cou + 1
    #print("shape ID %d" %(ID))
    return D, T, S, cou
