with open ("myfile.txt", "r") as fp:
    lines = fp.readlines()

    for i in range (len(lines)):
        print ("line" + str(i) + ":" + line)