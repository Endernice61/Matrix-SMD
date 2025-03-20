import sys
import read_matrix
import smd.transform

try:
    source_file_input_string = sys.argv[1]
except:
    print("Please enter the file you would like to transform: ")
    source_file_input_string = input()

try:
    source_f = open(source_file_input_string)
except:
    print("File failed to open")
    exit()

try:
    transformed_file_input_string = source_file_input_string.replace(".smd","_transformed.smd")
    if (transformed_file_input_string == source_file_input_string): raise Exception()
    transformed_file = open(transformed_file_input_string,"w")
except:
    print("The file is not an .smd")
    source_f.close()
    exit()

transformation = read_matrix.read_matrix()

def read_to(input_f,output,stop_string):
    line = input_f.readline()
    while (line != '' and line != stop_string):
        output.write(line)
        line = input_f.readline()
    output.write(line)

###Animations with rotation will not be fully supported
read_to(source_f,transformed_file,'skeleton\n')
line = source_f.readline()
while (line != '' and line != 'end\n'):
    if (line.startswith('  time')):
        transformed_file.write(line)
    else:
        transformed_file.write("  " + smd.transform.transform_vertex(line,transformation))
    line = source_f.readline()
transformed_file.write(line)


line = source_f.readline()
if (line != ''):
    transformed_file.write(line)
    line = source_f.readline()
    while (line != '' and line != 'end\n'):
        transformed_file.write(line)
        smd.transform.transform_triangle(source_f,transformed_file,transformation)
        line = source_f.readline()
    transformed_file.write(line)

source_f.close()
transformed_file.close()
