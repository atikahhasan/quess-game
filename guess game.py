

import random

def main():
    """start a elements guessing game,"""
    print("Guess the elements!")

    elements =[
        "hydrogen",
        "sodium",
        "zink",
        "mercury",
        "silicon",
        "carbon",
        "titanium",
        ]

    x = random.choice(elements)
    if x == "hydrogen":
        print("unsur teringan dunia")
    elif x == "sodium":
        print("mineral yang harus dimiliki tubuh agar berfungsi dengan baik")
    elif x == "zink":
        print("menjaga daya tahan tubuh")
    elif x == "mercury":
        print("logam yang mencemari air")
    elif x == "silicon":
        print("unsur kimia")
    elif x == "carbon":
        print("batu bara")
    elif x == "titanium":
        print("logam transisi yang ringan")
    guess = None

    while x != guess:

        guess = str(input("apakah elements yang saya fikir?"))

        if x == guess:
            print("you guessed{}.ANDA BERJAYA".format(guess))
            break
        else:
            print("you guessed{}.SILA CUBA LAGI!".format(guess))

main()
        

        
    
        
