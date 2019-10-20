from Find_neighbour import find_neighbour
def find_path(D, i, j):
    shp = [[i,j]]
    while len(shp) < 4: #continue until four nodes are found
        nei = []
        for point in shp:
            nei = nei + find_neighbour(D, shp, point[0], point[1], nei) #find all the possible neighbours with the current "shape"
        if nei == []:
            break
        nei.sort(key=lambda row: row[2]) #sort all the possible nodes by degree
        
        #if (nei[0][2] == nei[1][2]): #if there are neighbours with the same connectivity
            
            #find_neighbour(D, shp, point[0], point[1], nei)
        #else:
        shp.append([nei[0][0], nei[0][1]]) #add the lowest degree node to the shape
    return shp

