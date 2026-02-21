# lista
posts = []

while True:  # meny
    print("1. Lägg till post: ")
    print("2. Visa poster")
    print("3. Sök poster")
    print("4. Ta bort post")
    print("5. Avsluta")
    choice = int(input("Gör ett val: "))

    # läs in namn
    if choice == 1:  # lägga till en post i listan
        while True:
            name = input("Namn: ").strip()  # fråga efter namn

            if not name:
                print("Du måste fylla i ett namn")
            else:
                print("Namnet är godkänt")
                break

        # läs in telefonnummer
        while True:
            phonenr = input("Telefonnummer: ")
            if not phonenr:
                print("Du måste fylla i ett telefon nummer")

            # kolla att alla tecken är siffror
            elif not phonenr.isdigit():
                print("Telefonnumret får bara innehålla siffror")
            else:
                print("Telefonnumret är godkänt")
                break

        posts.append({"namn": name, "telefon": phonenr})
        print(f"Namn: {name} Telefonnummer: {phonenr} har lagts till! ")

    # visa alla poster
    if choice == 2:
        if not posts:
            print("Inga poster i registret. ")
        else:
            print("Alla poster i registret:")
            for i, post in enumerate(posts, start=1):
                print(
                    f"{i}. Namn: {post['namn']}, Telefonnummer: {post['telefon']}")

    # sök poster
    if choice == 3:
        if not posts:
            print("Inga poster i registret.")
        else:
            search = input(
                "Skriv ett namn eller telefonnummer att söka: ").strip().lower()

            resultat = []

            # loopa igenom alla poster
            for post in posts:
                namn = post['namn'].lower()
                telefon = post['telefon']
                if search in namn or search in telefon:
                    resultat.append(post)

            # visa resultat
            if not resultat:
                print("inga matchande poster hittades")
            else:
                print("Matchande poster:")
                for i, post in enumerate(resultat, start=1):
                    print(
                        f"{i}. Namn: {post['namn']}, Telefonnummer: {post['telefon']}")
    if choice == 4:
        if not posts:
            print("Finns inga poster att ta bort")
        else:
            while True:
                print("Alla poster i registret")
                for i, post in enumerate(posts, start=1):
                    print(
                        f"{i}. Namn: {post['namn']} Telefonnummer: {post['telefon']}")
                remove = input(
                    "Ange numret eller namnet på posten som ska tas bort: ").strip()
                if remove.isdigit():  # om användaren skriver en siffra
                    index = int(remove) - 1
                    if 0 <= index < len(posts):
                        removed_post = posts.pop(index)
                        print(
                            f"Posten '{removed_post['namn']}' har tagits bort!")
                        break  # Avbryter loopen
                    else:
                        print("ogiltigt nummer, försök igen")

                else:  # Tolkar annars inmatning som namn
                    found = False
                    for post in posts:
                        if post['namn'].lower() == remove.lower():
                            posts.remove(post)
                            print(f"Posten '{post['namn']}' har tagits bort!")
                            found = True
                            break
                    if found:
                        break  # Bryter bara borttagningsloopen
                    else:
                        print("Namnet finns inte, försök igen.")
    if choice == 5:
        break
