fo = open("day1prac.txt", "r")
lines = fo.readlines()
lastnum = 0
for line in lines:
    print(line.strip())
    if(int(line.strip()) > lastnum):
        print("increase")
    else:
        print("decrease")
    lastnum = int(line.strip())
    print("*************")
