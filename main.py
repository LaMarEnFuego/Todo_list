import json


def show_menu():
    print("\nPlease select from the following menu:\n")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Delete task")
    print("4. Exit application")


def load_tasks():
    try:
        with open("saved_tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks


def add_task(tasks):
    new_task = input("\nEnter your task: ")
    tasks.append(new_task)
    with open("saved_tasks.json", "w") as file:
        json.dump(tasks, file)
    print(f"\nAdded {new_task} to your list.")


def view_tasks(tasks):
    if not tasks:
        print("\nThere are no tasks in the list")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}, {task}")


def delete_task(tasks):
    if not tasks:
        print("\nThere are no tasks in the list")
    else:
        view_tasks(tasks)
        target = int(input("\nWhich task number would you like to delete: "))
        if 1 <= target <= len(tasks):
            deleted_task = tasks.pop(target - 1)
            with open("saved_tasks.json", "w") as file:
                json.dump(tasks, file)
            print(f"\nTask {deleted_task} deleted.")
        else:
            print("Invalid task number")


def main():
    print("\nWelcome to a simple To-Do list practice app!")
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Your option choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print('Thank you for using my application.  Goodbye!')
            break
        else:
            print('\nPlease select a valid option, or press 4 to end.')


if __name__ == "__main__":
    main()
