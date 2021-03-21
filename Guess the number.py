import random

print("Hola, ¿cómo te llamas?")
name = input()

print("Bueno," + name + ", estoy pensando en un número del 1 al 20")
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print("¿Qué número es?")
    guess = int(input())

    if guess < secretNumber:
        print("Más alto.")
    elif guess > secretNumber:
        print("Más bajo")
    else:
        break #This condition if for the correct guess!

if guess == secretNumber:
    print("Genial," + name + ", has necesitado " + str(guessesTaken) + " intentos para adivinar el número.")
else:
    print("Vaya, estaba pensando en " + str(secretNumber))
