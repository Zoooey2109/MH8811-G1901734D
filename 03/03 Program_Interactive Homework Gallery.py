
# Define greeting to world function
def gtw():
    print("Hello, world!")

# Define greeting to you function
def gty():
    name = input("What's your name?")
    print('Hello,' , name,'!')

# Define temperature transformation function
def tt():
    C = float(input("Please input degree in Celsius here: "))
    print("Converting Celsius to Fahrenheit:", C*1.8 + 32)

# Prompt user to choose
print("Which one do you want to run :")
print('\nInput 1 to run "greeting to world" function, \n\
Input 2 to run "greeting to you" function,\n\
Input 3 to run "temperature transformation" function,\n\
Input 0 to exit this program.')

# Run the chosen sub-program
# and go back to the stage where user is prompted to choose
while True:
    n = int(input("\nPlease enter your number: "))
    if n == 1:
        gtw()
        continue
    elif n == 2:
        gty()
        continue
    elif n == 3:
        tt()
        continue
    elif n == 0:
        from tkinter import messagebox
        messagebox.askokcancel("Exit?","Are you going to leave me? (ToT)")
        messagebox.showinfo("Info","Thank you for using this program :)")
        exit()
    else:
        print("Please enter the correct number!")
        continue
