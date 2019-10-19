import random

def genPassword(n):
    Randompwd = []
    global Uppercase, Lowercase, Digits, Symbols
    Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Lowercase = "abcdefghijklmnopqrstuvwxyz"
    Digits = "0123456789"
    Symbols = "~!@#$%^&*()_+=-\][';/.,`"
    for p in range(n):
        if p % 4 == 0:
            Randompwd.append(random.choice(Digits))
        if p % 4 == 1:
            Randompwd.append(random.choice(Symbols))
        if p % 4 == 2:
            Randompwd.append(random.choice(Lowercase))
        if p % 4 == 3:
            Randompwd.append(random.choice(Uppercase))
    random.shuffle(Randompwd)
    return("".join(Randompwd))

# main program
if __name__ == "__main__":
    print(genPassword(12))
