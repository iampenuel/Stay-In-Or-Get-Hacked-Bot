# STAY-IN-OR-GET-HACKED BOT (Lifestyle & Password bot...it will judge you *cue evil laugh*)

import random
import string

print("==============================================")
print("  WELCOME TO THE STAY-IN-OR-GET-HACKED BOT  ")
print("==============================================\n")

print("I'm here to tell you what to do with your day")
print("and whether your passwords are...como se dice...")
print("EMBARRASSING!")
print("Let's begin :) \n")

# === MOOD ===
# mood = input("So how are you feeling today...or tonight idk the time haha. How are ya? (e.g tired,happy,over-it): ").lower()

# === ENERGY ===
while True:
    try:
        energy = int(input("On a scale of 1–10, how much energy do you have right now?: "))
        if 1 < energy > 10:
            print("Oh my digital dayssss...I love you but dang my guy! On a scale of 1 TO 10!!! okay dear? try again. ")
            continue
        break
    except ValueError:
        print("My brethren in Christ! Whole Numbers please...numbers. Try again. \n")

# === MONEY ===
while True:
    try:
        money = float(input("\nHow much money do you have right now (just digits fam)? $: "))
        if money <= 0:
            print("Bruhhh... what are you doing outside? Go home. Sorry to say but I'm afraid you're broke :(")
        elif money <= 10:
            print("You going to the dollar store??? Walmart??...what's the plan homie? \n")
        elif money <= 100:
            print("You got some money to spenddd \n")
        else:
            print("Okay baller. We outside??? You got that money huh?? Go enjoy your money! \n")
        break
    except ValueError:
        print("Yeah...here we go with the not-numbers again. GIVE ME NUMBERSSSS! I need to calm down. My bad. Try again darling.")


# === PASSWORD ===
while True:
    password = input("Would you like a password while you're here? (yes/no): ").lower()
    if password == "yes":
        print("You're smart! Let's get you a password 🙂\n")
        break
    elif password == "no":
        print("Okay... but don’t come crying to me when you get hacked. Just saying 🤷\n")
        break
    else:
        print("Let's try this one more time, dear... it's a YES or NO question. Please and thank you.\n")

# === PASSWORD STRENGTH ===
while True:
    strength = input("How strong do you want your password? (weak / medium / strong): ").lower()
    if strength == "weak":
        characters = string.ascii_letters  # string.ascii_letters -> abcdef...XYZ
        length = 6
        print("Someone's about to get hacked but hey...who's judging? Not me...I'm just a bot after all 🤷")
        break
    elif strength == "medium":
        characters = string.ascii_letters + string.digits  # string.digits -> 0123456789
        length = 10
        print("That's fair...not too strong, not too weak. Just a cool in-between ya know. Let's get it!")
        break
    elif strength == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation # string.punctuation->!"#$%&'()*+,-./:;<~
        length = 16
        print("FINALLY! A sensible being! You got it champ...let's get you an unbreakable password!")
        break
    else:
        print("Bro...that’s not an option. Try again.")

# === RANDOM PASSWORD GENERATOR ===
password = ''.join(random.choices(characters, k=length))
print(f"\nHere's your password : {password}")
print("Better not forget it...or do. I can't really tell you what to do :)")