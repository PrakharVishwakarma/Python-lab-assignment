f = open("lab4file/demofile.txt", "a")
f.write("Now the file has more content!\n")
f.close()

f = open("lab4file/demofile.txt", "r")
print(f.read())
