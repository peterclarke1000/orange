
import sys

def main(option):

    if option == "zero":
        print("You typed zero.\n")
    elif option == "sqr":
        print("n is a perfect square\n")
    elif option  == "2":
        print("n is an even number\n")
    else:
        print("No correct options found")


if __name__ == '__main__':
    option = sys.argv[1]
    main(option)
