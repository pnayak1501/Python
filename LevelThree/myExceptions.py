
def main():
    try:
        myfile = open("C:/Users/prahl/Desktop/sasa.txt", "r")
        print("Successful reading")
        print(myfile.read())

    except IOError:
        print("Not able to open")

    print("Task Done")


if __name__ == "__main__":
    main()
