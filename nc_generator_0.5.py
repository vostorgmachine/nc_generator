# --------------------------------------------------------------------------------
# GOALS: 
# Make full .nc-end generator(?)
# --------------------------------------------------------------------------------
import inspect
import os
print("-------------------------")
print("NC generator v.0.5(alpha)")
print("-------------------------")
print()

main_folder = "/home/vostorg/python/nc_generator/source/"

handle = str(input("Enter the model of handle: "))
handle_model = handle
path = main_folder+str(handle)+str("/")

size = int(input("Enter the size of handle: "))
handle = str(size) + str("_") + handle
handle_size = handle
path = path + handle

pi = int(input("Enter the pi: "))
pi = str("_")+str(pi)+str("pi")
path = path+pi+str("/")

# this func making selected dir is current for code
os.chdir(path)

# this one scans a directory and making a list of included files:
only_files = [f for f in os.scandir(path) if f.is_file()]

# --------------------------------------------------------------------------------
def nc_end_line():
    f.write('\n'"")
    f.write('\n'"(=============================================)")
    f.write('\n'"")

def sep_line():
    print("")
    print("------------------------------ ")

sep_line()
print ("Selected directory: ")
print (path)

sep_line()
print("Files in direcroty: ")
print("")
def cont_display(only_files):
    c = 0
    n = c+1
    while c < len(only_files):
        print('[  '+str(n)+'  ]')
        print(only_files[c] )
        print("")
        c+=1
        n+=1

cont_display(only_files)
sep_line()

selected_file = int(input("Select the file u want to work with: "))
selected_file = selected_file-1

print("")
print("Selected file: ")
print(only_files[selected_file])
print("")

work_zero_num = str(input("Enter the number of work zero (from 1 to 5): "))
work_zero_num = int(work_zero_num)+3

work_zero = str("G5")+str(work_zero_num)
print("")
print("Selected work zero is: ", work_zero)

# --------------------------------------------------------------------------------
def end_result():
    f.write(str("(")+handle_size+str(")"))
    f.write('\n')
    f.write(''.join(work_zero)+str(" "))
    f.write('')
    f.write('\n'.join(selection))
    nc_end_line()
# --------------------------------------------------------------------------------

if handle_model == 'long':
    nc_head = str("G00 G49 G40.1 G17 G80 G50 G90")
    with open(only_files[selected_file] , 'r') as f:
        content = f.read().splitlines()
    selection = content[content.index(nc_head):content.index("M30")-1]
    with open('/home/vostorg/python/nc_generator/blank.nc', 'a') as f:
        end_result()
        print("")
        print("Done!")
        exit()

# --------------------------------------------------------------------------------

print("")
instance_number = int(input("How much instances: "))
instance_number = str("(INSTANCE #: ")+str(instance_number+1)+str(")")

nc_head = str("G00 G49 G40.1 G17 G80 G50 G90")
with open(only_files[selected_file] , 'r') as f:
    content = f.read().splitlines()
selection = content[content.index(nc_head):content.index(instance_number)-1]
with open('/home/vostorg/python/nc_generator/blank.nc', 'a') as f:
    end_result()

print("")
print("Done!")
