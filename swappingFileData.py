# Creating a function to swap the data of textFile1 and textFile2

def swappingFileData():
    data = ""
    with open("textFile1.txt","r") as a :
        data_a = a.read()

    with open("textFile2.txt","r") as b :
        data_b = b.read()
    
    with open("textFile1.txt","w") as a :
        a.write(data_b)

    with open("textFile2.txt","w") as b :
        b.write(data_a)

    del data

swappingFileData()