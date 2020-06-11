
def main():
    # file = open("lco.txt", "w+")
    # for i in range(20):
    #     file.write("Hello Prahlad %d \n" % (i))
    # file.close()
    file = open("lco.txt","r")
    if file.mode == "r":
        for line in file.read():
            print(file.read())
    file.close()


if __name__ == "__main__":
    main()