import serial

port = 'COM3'
ard = serial.Serial(port,9600)

username = "team5"
password = "kstate2020"

print("Please sanitize your hands to log in!")

i = 1

while (i < 2):
    msg = ard.readline() #Reading COM3 Port via serial communication
    msg = msg.decode('Ascii') #This line decodes message
    msg = int(msg) #Cast msg as integer
    if (msg == 1234):
        print("Thank you for sanitizing your hands!")
        username_input = input("Please enter your username: ")
        password_input = input("Please enter your password: ")
        if username_input == username and password_input == password:
            reset = input("Would you like to logout? Y/N: ")
            if reset == "Y":
                print(" ")
                print("Logout successful")
                print("")
                print("PLEASE SANITIZE YOUR HANDS!")
            else: 
                reset = input("Select Y when ready to logout: ")
                if reset == "Y":
                    print(" ")
                    print("Logout successful")
                    print("")
                    print("PLEASE SANITIZE YOUR HANDS!")      
        else:
            print("Invalid login")
            print("")
            print("PLEASE SANITIZE YOUR HANDS!")
            
        msg = 1

    else:
        print("PLEASE SANITIZE YOUR HANDS!")