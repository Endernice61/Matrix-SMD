import linear_transformation

def transform_vertex(input_string,transformation):
    data = input_string.rsplit()
    i = 4
    tail = ""
    while (i<len(data)):
        tail += " " + data[i]
        i += 1
    vec = linear_transformation.transform(transformation,[float(data[1]),float(data[2]),float(data[3])])
    return f"  {data[0]} {vec[0]:.6f} {vec[1]:.6f} {vec[2]:.6f}{tail}\n"

def transform_triangle(input_f,output,transformation):
    output.write(transform_vertex(input_f.readline(),transformation))
    output.write(transform_vertex(input_f.readline(),transformation))
    output.write(transform_vertex(input_f.readline(),transformation))
