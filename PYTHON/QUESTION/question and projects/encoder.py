#encode the given message
def main():
    print("the program converts a textual message into a sequence")
    print("of numbers reprsenting the unicode encoding of the message.")

    message = input("enter the number you want to encode:")

    print("\nHere are the Unicode codes:")

    for ch in message:
        print(ord(ch), end=" ")


main()