import os
Todo = []


def clear_screen():
    if os.name == 'nt':
        os.system("cls")


while True:
    clear_screen()
    print("Todo-list")
    print("1. Show list")
    print("2. Add to list")
    print("3. Exit")
    try:
        choice = int(input("Make a selection: "))
    except ValueError:
        print("Please make a valid choice")
        print("Press enter to continue")
        continue

    if choice == 1:
        if not Todo:
            print("Nothing is in the list")
        else:
            print("Everything in the Todo-list")
            for i, task in enumerate(Todo, start=1):
                print(f"{i}. {task}")

            input("Press enter to continue...")

    elif choice == 2:
        print("Please enter the task you want to add:")
        task = input().strip()
        Todo.append(task)

    elif choice == 3:
        break
