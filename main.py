''' Rosalinda Phipps '''

def encoder(password):
    new_password = ''
    for i in range(0, len(password)):
        new_password += str((int(password[i])+3)%10)
    return new_password

def menu():
    print("Menu \n-------------")
    print("1. Encode\n2. Decode\n3. Quit\n")

if __name__ == "__main__":
    run = True

while run:
    menu()
    user_select = int(input("Please enter an option: "))

    if user_select == 1:
        user_password = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!\n")

    if user_select == 2:
        print(f"The encoded password is {encoder(user_password)}", end='')
        print(f", and the original password is {user_password}.\n")

    if user_select == 3:
        break
