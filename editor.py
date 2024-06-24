import os 


filename = input("nombre del archivo a crear: ")


create = open(filename,'w')


with open(create.name, 'r+') as arch:
  add = arch.write()
  