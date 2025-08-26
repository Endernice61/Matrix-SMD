def transform(matrix,vector):
    def apply(row,vec):
        component = 0
        for j,k in zip(row,vec):
            component += j*k
        return component
        
    out = []
    try:
        for i in matrix:
            out.append(apply(i,vector))
    except:
        raise Exception("Failed to apply the matrix to the vector")
    return out

def invert(matrix):
    if (len(matrix) != len(matrix[0])): raise Exception("Not a square matrix!")
    try:
        ident = identity(len(matrix))
        inverted = row_reduce_mirror(matrix[:],ident)
    except:
        raise Exception("Coud not invert matrix")
    return inverted

def truncated(matrix,x,y):
    truncated = matrix[:y]
    i = len(truncated)-1
    while (i >= 0):
        truncated[i]=truncated[i][:x]
        i -= 1
    return truncated

def row_reduce_mirror(matrix,mirror,d=0):
    if (matrix[d][d] == 0):
        u = d
        while (u<len(matrix)):
            if (matrix[u][d] != 0):
                matrix[d],matrix[u] = matrix[u],matrix[d]
                mirror[d],mirror[u] = mirror[u],mirror[d]
                break
            u += 1
        if (u == len(matrix)):
            raise Exception("Could not row reduce")
    u=d
    scale = 1/matrix[d][d]
    while (u<len(matrix[d])):
        matrix[d][u] *= scale
        mirror[d][u] *= scale
        u += 1
    u=d+1
    while (u<len(matrix)):
        v=d
        scale = matrix[u][d]
        while (v<len(matrix[d])):
            matrix[u][v] -= scale*matrix[d][v]
            mirror[u][v] -= scale*mirror[d][v]
            v += 1
        u += 1
    d += 1
    if (d<len(matrix) and d<len(matrix[d])):
        return row_reduce_mirror(matrix,mirror,d)
    return mirror

def identity(x):
    ident = []
    u = 0
    while (u<x):
        ident.append([])
        v=0
        while (v<x):
            if (u == v): ident[u].append(1)
            else: ident[u].append(0)
            v += 1
        u += 1
    return ident

def transpose(matrix):
    transposed = []
    u = 0
    while (u<len(matrix[0])):
        transposed.append([])
        for v in matrix:
            transposed[u].append(v[u])
        u += 1
    return transposed
