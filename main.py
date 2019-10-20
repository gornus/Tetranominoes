# ####################################################
# DE2-COM2 Computing 2
# Individual project
#
# Title: MAIN FILE
# Authors: Gordon Cheung Yat Hei (CID: 01083012)
# Last updated: 7th December 2017
# ####################################################

from Read_degree import read_degree
from Find_Path import find_path
from Brute_Place import brute_place
from Place_Shape import place

def Tetris(target):
    print("starting")
    y_len = len(target) #read the dimensions of the target matrix
    x_len = len(target[0])
    solution = [[(0, 0) for j in range(x_len)] for i in range(y_len)] #create the solutio nmatrix with all (0,0) tuple
    degree = read_degree(target) #feed target into the read_degree function to create the matrix recording degree of all nodes
    count = 1 #initialises the shape count

    for i in range(y_len): #loop through the whole matrix
        for j in range(x_len):
            if degree[i][j] == 0: #if the degree of the node is 0, it is an isolated node, ignore
                # print("0 is found")
                target[i][j] = 0
                degree[i][j] = float('inf')
                #solution[i][j] = (0, 0)
            elif target[i][j] == 1: #if the node is a block need to be placed
                shape = find_path(degree, i, j) #feed into the find_path function to find the best shape for the node
                # print (shape)
                # print (shape_deg)
                if len(shape) == 4: #if the returned shape has four nodes, place the shape
                    degree, target, solution, count = place(degree, target, solution, shape, count)
                elif len(shape) < 4: #brute place the shape if shape has less than four nodes
                    degree, target, solution, count = brute_place(degree, target, solution, shape, count)

        #print("count %d"%(count))

    return solution

