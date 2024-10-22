import random
secret_number = random.randint(0,20)
intents = 3

while intents >0:

    user_number = int(input("Adivina el numero entre el 0 y el 20: "))
    distance = abs(secret_number - user_number)

    if secret_number == user_number:
        print("¡Felicitaciones! ¡Has adivinado el número!")
        break
    
    elif distance <3:
        print("¡Caliente, caliente!")

    elif distance >=3 and distance <=6:
        print("¡Tibio, tibio!")

    else: 
        print("¡Frío,frío!")

    intents -=1

if intents == 0:
    print(f"Lo siento, no adivinaste el número. El número correcto era {secret_number}.")
