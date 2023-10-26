import random

lives = 4
lists = ["CODIGO", "JAVA", "PROGRAMA", "COMPUTADORA"]
word_random = random.choice(lists)
print("BIENVENID@ AL AHORCADO\n Intente adivinar la palabra relacionada a la programacion: (tiene 4 intentos)")

word_guess = ["_"]*len(word_random)
print('Letras: ', " ".join(word_guess))

while lives!=0:
    letter = input("Ingrese letra: ").upper()
   
    if letter in word_random:
        if letter == word_random:
            for i in range(0, len(word_random)):
                word_guess[i] = word_random[i]
            print(" ".join(word_guess))
            break
        for i in range(0, len(word_random)):
           if letter == word_random[i]:
               word_guess[i] = letter
    else:
       lives-=1
    print('Palabra: ', " ".join(word_guess))

    if "".join(word_guess) == word_random or letter == word_random:
        break

if lives == 0:
    print(f"Perdiste! La palabra era: {word_random}")
else:
    print("¡Felicitaciones, GANASTE!")