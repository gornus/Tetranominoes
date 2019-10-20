def find_neighbour(D, shape, i, j, n):
    y_len = len(D)
    x_len = len(D[0])
    neighbour = [] #initialise the list of possible neighbours

    if i + 1 < y_len: #check the neighbouring node if that is valid, append it to the list if it is a node need to be placed
        if D[i + 1][j] < float('inf') and [i+1,j] not in (shape + n):
            neighbour.append([i+1,j, D[i+1][j]])
    if j + 1 < x_len:
        if D[i][j + 1] < float('inf') and [i,j+1] not in (shape + n):
            neighbour.append([i,j+1, D[i][j+1]])
    if i - 1 >= 0:
        if D[i - 1][j] < float('inf') and [i-1,j] not in (shape + n):
            neighbour.append([i-1,j, D[i-1][j]])
    if j - 1 >= 0:
        if D[i][j - 1] < float('inf') and [i,j-1] not in (shape + n):
            neighbour.append([i,j-1, D[i][j-1]])
    return neighbour