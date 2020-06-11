import db_helper


def main():
    run = 1
    db_helper.create_table()
    while run:
        print()
        print("1. Insert a new task in the todo list \n"
              "2. View the todo list\n"
              "3. Delete the task\n"
              "4. Exit\n")
        x= int(input("Choose any of the above option "))

        if x==1:




if __name__ == "__main__":
    main()
