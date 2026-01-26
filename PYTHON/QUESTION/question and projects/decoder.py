# decode the given msg
def main():
    print("the program converts a sequence of unicode number into")
    print("the string of text that it represents.\n")

    inString=input("enter the unicode- decode:")
    message=""

    print("\nHere are the Unicode codes:")

    for numstr in inString.split():
        Codenum=int(numstr)
        message=message+chr(Codenum)
        print(message)

main()        