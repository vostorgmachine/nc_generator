# --------------------------------------------------------------------------------
# Changelog
# --------------------------------------------------------------------------------
# O.7:
#>> Now last func are separated between handles that include
#   instances and other
#
# 0.8:
#>> Добавлена работа с инстанциями + параметр [f]ull
#>> При работе с рондо автоматом игнорируется параметр pi
#>> Добавлен модуль colorama. Теперь на выходе есть цветной текст
#>> Добавлено слияние имени и кол-ва инстанций
#
# 0.9:
#>> Добавлен счетчик инстанций
#
# --------------------------------------------------------------------------------
# GOALS: 
#
# --------------------------------------------------------------------------------
# BUGS:
#>> При вводе текста в поле size не срабатывает цикл. Вылетает програма
#
#>> Во все запросы можно ввести отрицательные знач-ия и это не будет считаться
#>> ошибкой

from colorama import *
import colorama
import inspect
import os

colorama.init(autoreset=True)

print(Fore.CYAN + "NC generator v.0.9(alpha)")
print()

def error_message(res):
    print(Fore.RED + "Please enter the correct " + res + " of handle")
    print() 

def sep_line():
    print()
    print("------------------------------ ")

# main_folder = "/mnt/c/Users/vostorg/Documents/nc resource/"
main_folder = "/home/vostorg/python/nc_generator/nc resource/"

handles_group1 = ["grand", "bruno", "aero",
          "bridge", "arks", "long", "rondo"
                 ] 
handles_sizes = [120, 168, 200, 296, 904, 1032 ]

print(Fore.YELLOW + "Handles that included for now in list : ")
print(handles_group1)
print()

while True:
    handle = str(input("Enter the model of handle: "))
    if handles_group1.count(handle) == 1:
        handle_model = handle
        path = main_folder+str(handle)+str("/")
        break
    else:
        error_message("name")

print() 
print(Fore.YELLOW + "Sizes that included for now in list : ")
print(handles_sizes)
print()

if handle_model == "rondo":
    while True:
        size = int(input("Enter the size of handle: "))
        if handles_sizes.count(size) == 1:
            handle = str(size) + str("_") + handle 
            handle_size = handle
            handle = handle + str("/")
            path = path + handle
            break
        else:
            error_message("size")

else:
    while True:
        size = int(input("Enter the size of handle: "))
        if handles_sizes.count(size) == 1:
            handle = str(size) + str("_") + handle
            handle_size = handle
            path = path + handle
            while True:
                print() 
                pi = int(input("Enter the pi: "))
                if pi <= 5 :
                    pi = str("_")+str(pi)+str("pi")
                    path = path+pi+str("/")
                    break
                else:
                    print(Fore.RED + "Probably there is a mistake here" )
            break
        else:
            error_message("size")

# this func making selected dir is current for code
os.chdir(path)

# this one scans a directory and making a list of included files:
only_files = [f for f in os.scandir(path) if f.is_file()]

# --------------------------------------------------------------------------------

def cont_display(only_files):
    global c, n
    c = 0
    n = c+1
    while c < len(only_files):
        print('[  '+str(n)+'  ]')
        print(only_files[c] )
        print("")
        c+=1
        n+=1

sep_line()
print (Fore.GREEN + "Selected directory: ")
print (path)

sep_line()
print(Fore.GREEN + "Files in direcroty: ")
print("")

cont_display(only_files)
sep_line()

while True:
    selected_file = int(input('Select the file u want to work with: '))
    if selected_file <= c:
        selected_file = selected_file-1
        print()
        print(Fore.GREEN + "Selected file: ")
        print(only_files[selected_file])
        print()
        break
    else:
        print(Fore.RED + "Please enter the number from 1 to " + str(c))
        print() 

file_chosing = str(path) + str(only_files[selected_file])
while True:     
    work_zero_num = int(input("Enter the number of work zero (from 1 to 5): "))
    if work_zero_num <= 5:
        work_zero_num = int(work_zero_num)+3
        work_zero = str("G5")+str(work_zero_num)
        print("")
        print(Fore.GREEN + "Selected work zero is: ", work_zero)
        break
    else:
        print(Fore.RED + "Please enter the number from 1 to 5")
        print() 

# --------------------------------------------------------------------------------

nc_head = str("G00 G49 G40.1 G17 G80 G50 G90")

# blank = "/mnt/c/Users/vostorg/Documents/nc resource/blank.nc"
blank = "/home/vostorg/python/nc_generator/nc resource/blank.nc"

def slicing_func(last_point):
    with open(only_files[selected_file] , 'r') as f:
        content = f.read().splitlines()
    selection = content[content.index(nc_head):content.index(last_point)-1]
    with open(blank, 'a') as f:
        if handle_model == "rondo":
            f.write(str("(")+handle_size+str(" with"))
        else:
            f.write(str("(")+handle_size+str(pi)+str(" with"))
        f.write(str(" ")+instance_number_natural+str(" instances in block)"))
        f.write('\n')
        f.write(''.join(work_zero)+str(" "))
        f.write('\n'.join(selection))
        f.write('\n'"")
        f.write('\n'"(=============================================)")
        f.write('\n'"")

if handle_model == 'long':
    slicing_func("M30") 

else:
    print("")
    print (Fore.YELLOW+ "Chose [f]ull to include whole file")

# instance_counter section
    f = open(only_files[selected_file] , 'r') 
    data=[] 
    flag=False
    with f as f:
        for line in f:
            if line.startswith("(INSTANCE"):
                flag = True
            if flag:
                data.append(line)
            if line.strip().endswith(")"):
                flag=False
    print() 
    print (Fore.BLUE + (data)[-1] + str("is the last instance in file") )
    print() 

    instance_number = str(input("How much instances: "))
    instance_number_natural = instance_number
    if instance_number_natural == "f":
        instance_number_natural = "all"

    if instance_number == "f":
        slicing_func("M30")
    else:
        instance_number = int(instance_number)+1
        instance_number = str("(INSTANCE #: ")+str(instance_number)+str(")")
        slicing_func(instance_number)

print("")
print("Done!")
exit()
