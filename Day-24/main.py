file = open("my_file.txt")
content = file.read()
print(content)
file.close()
#With the above method we have to close the file manually after reading the content

with open("my_file.txt",'a') as file:
    file.write("currently I'am Learning Python")

 # But By using this one we are no longer required to close the file
                                 