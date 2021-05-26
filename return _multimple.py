### THIS IS JUST  TO SHOW THTA A Function can return multiple values

#ADDING MACHINE



def adding_machine():
    amount = 0

    while True:
        b, n = get_input()
        if not b:
            break
        amount += n
    print("TOTAL: ", amount)



def get_input():
    i = input("Enter Num: ")
    if not i:
        return False, 0
    return True, float(i)


adding_machine()