import random

secretnr = random.randint(1, 200)

attempt = 0

guesses = []
guesses.sort()
while attempt < 10:  # loop för att göra 10 försök
    try:  # Fångar fel
        guess = int(input(f"Försök {attempt + 1}/10 Gissa talet: "))
    except ValueError:
        print("Skriv ett heltal")
        continue
    if guess > 200:
        print("Intervallet är 1-200, försök igen")

    guesses.append(guess)
    attempt += 1  # Ökar bara efter giltig inmatning

    if guess > secretnr:
        print("Talet är för högt")
    elif guess < secretnr:
        print("Talet är för lågt")
    else:
        guesses.sort()
        print(f"Du gissade rätt! Det hemliga talet var {secretnr}")
        print(f"Dina gissningar: {guesses}")
        break
else:
    guesses.sort()
    print(f"Du har slut på försök. Rätta talet var {secretnr}")
    print(f"Dina gissningar: {guesses}")
