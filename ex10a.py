file = open("demo.txt", "w")                     
file.write("Hello, this is a file handling\n")
file.write("Python")                             
file.close()                                     

file = open("demo.txt", "r")                     
print("Reading from the file:")
print(file.read(), end=" ")                      
file.close()                                     
