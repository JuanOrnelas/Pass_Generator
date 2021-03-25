import random
import string

chars="abcdefghijklmñnopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ123456789#&/$!_(?-#)¡"
chars2=string.printable

#In this case you can use chars or chars 2 and obtain the same result

while 1:
    password_len = int(input("Insert the length of your password: "))
    password_count =int(input("Number of passwords do you like? "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password_char2 = random.choice(chars2)
            password = password + password_char + password_char2
        print("This is your password: ",password)
        
