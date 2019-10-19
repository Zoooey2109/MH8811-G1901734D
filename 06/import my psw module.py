import psw as p

imput_psw = int(input("Which password length do you want: "))
print("Your random password is : {}".format(p.genPassword(imput_psw)))
