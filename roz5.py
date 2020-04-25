file_name = "rozal5.txt"
file_name2 = "rozal5exit.txt"
f = open(file_name, "r")
d = open(file_name2, "w")
a = 0
for i in f:
    print(i)
    if a % 2 == 1:
        d.write(i)
    a += 1
f.close()
d.close()
