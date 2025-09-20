x=open("new-file.txt","w")
x.write("Hello world")
x.close()


with open("new-file.txt","a") as l:
    l.write("\n hello python \n")
    l.write("Hello Amma \n")

with open("new-file.txt","r") as f:
    y=f.read()
    print(y)
    f.close()

with open("sec-file.txt","w") as f:
    f.write(y)

with open("sec-file.txt","r") as f:
    print("this is the content in the second file")
    print(f.readlines())