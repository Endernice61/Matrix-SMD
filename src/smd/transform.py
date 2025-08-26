import matrix

def transform_vertex(input_string,transformation,normal=None):
    data = input_string.rsplit()
    i = 7
    tail = ""
    while (i<len(data)):
        tail += " " + data[i]
        i += 1
    if (len(transformation[0])==4):
        vec = matrix.transform(transformation,[float(data[1]),float(data[2]),float(data[3]),float(1)])

    else:
        vec = matrix.transform(transformation,[float(data[1]),float(data[2]),float(data[3])])
    if (normal is None): norm = [float(data[4]),float(data[5]),float(data[6])]
    else: norm = matrix.transform(normal,[float(data[4]),float(data[5]),float(data[6])])
    return f"  {data[0]} {vec[0]:.6f} {vec[1]:.6f} {vec[2]:.6f} {norm[0]:.6f} {norm[1]:.6f} {norm[2]:.6f}{tail}\n"

def transform_triangle(input_f,output,transformation,normal=None):
    output.write(transform_vertex(input_f.readline(),transformation,normal))
    output.write(transform_vertex(input_f.readline(),transformation,normal))
    output.write(transform_vertex(input_f.readline(),transformation,normal))
