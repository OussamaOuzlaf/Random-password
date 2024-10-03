import pyautogui
import random

character = "0123456789azertyuiopqsdfghjklmwxcvbn"
character_list = list(character)

password = pyautogui.password("Enter password here: ")
guess_password = ""

while(guess_password!=password):
    guess_password = random.choices(character_list, k=len(password))
    print(">>>>>"+str(guess_password)+"<<<<<")
    if(guess_password==list(password)):
        print("Your password is: " + "" .join(guess_password))
        break;