import random

randomnr = []  # lista för de slumpade talen

while len(randomnr) < 7:  # loop för att slumpa 7 tal
    tal = random.randint(1, 50)
    if tal not in randomnr:  # if för att inte skapa dubletter
        randomnr.append(tal)
        continue

usernr = []

while len(usernr) < 7:
    try:
        usertal = int(input(f"Ange tal {len(usernr) + 1}: "))
    except ValueError:
        print("Text är ej tillåten")
        continue
    if usertal < 1 or usertal > 50:
        print("Talet måste vara mellan 1 och 50")
        continue
    elif usertal in usernr:
        print("du får inte ange samma tal två gånger")
        continue
    else:
        print("Talet är godkänt")
        usernr.append(usertal)

randomnr.sort()
usernr.sort()
correct = [usertal for usertal in usernr if usertal in randomnr]

print(f"Dina nummer är {usernr}")
print(f"Rätt lotto rad {randomnr}")
print("Rätt gissade tal:", correct)
print(f"Antal rätt:", len(correct))
