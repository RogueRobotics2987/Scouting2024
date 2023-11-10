while True:

    qrinput=input("Enter Your Input")
    #print(qrinput

    print(qrinput)
    with open("C:\\Users\\Rogue\\PycharmProjects\\pythonProject\\AllData.csv", "a") as allData:
        allData.write(str(qrinput)+"\n")
