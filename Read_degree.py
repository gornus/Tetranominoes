import numpy as np

def read_degree(inp):
    y_len = len(inp)
    x_len = len(inp[0])
    #print(y_len, x_len)
    oup = np.zeros((y_len, x_len))
    _ = float('inf')  # Definition of infinity
    for i in range(y_len):
        for j in range(x_len):
            deg = 0
            #print("Current Block %d %d: %d" % (i, j, inp[i][j]))
            if inp[i][j] == 1:
                if i+1 < y_len:
                    if inp[i+1][j] == 1:
                        deg = deg + 1
                    #print("block_down %d %d: %d" % (i + 1, j, inp[i + 1][j]))
                if i-1 >= 0:
                    if inp[i-1][j] == 1:
                        deg = deg + 1
                    #print("block_above %d %d: %d" % (i - 1, j, inp[i - 1][j]))
                    #print(inp[i-1][j])
                if j+1 < x_len:
                    if inp[i][j+1] == 1:
                        deg = deg + 1
                    #print("block_right %d %d: %d" % (i, j + 1, inp[i][j + 1]))
                if j-1 >= 0:
                    if inp[i][j-1] == 1:
                        deg = deg + 1
                    #print("block_left %d %d: %d" % (i, j - 1, inp[i][j - 1]))
                    #print(inp[i][j-1])
                oup[i][j] = deg
            else:
                oup[i][j] = _
    return oup