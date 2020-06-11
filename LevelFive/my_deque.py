from collections import deque
import string

def main():
    myd = deque(string.ascii_lowercase)
    print("Number of elements:",len(myd))

    for i in myd:
        print(i,end=",")
    print()
    # print(myd.pop())
    # print(myd)
    # print(myd.popleft())
    # myd.append(111)
    # print(myd)
    myd.rotate(5)



if __name__ == "__main__":
    main()