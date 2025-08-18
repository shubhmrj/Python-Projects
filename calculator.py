a = int(input("Enter the first input:"))
b = int(input("Enter the second input:"))

c = int(input("enter the choice: "))

def addition():
    add = a+b
    return add
def substraction():
    sub = a-b
    return sub
def multiplication ():
    mul = a*b
    return mul
def division ():
    div= a/b
    return div

cont = input("you want to continue press yes otherwise no : ")
while cont == 1:
    def match():
        match c:
            case 1:
                return addition()
            case 2:
                return substraction()
            case 3:
                return multiplication()
            case 4:
                return division()
            case _:
                print("you entered wrong case.")
        return match()


    print(match())
cont = input("you want to continue press yes otherwise no : ")










