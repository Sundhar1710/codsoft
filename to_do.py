def todo():
    print("Welcome to To-Do List App")

def show(task):
    if not task:
        print("The list is empty...")
    for i in task:
        print(f"{i}\r")
    print("---------------------\n")

def add(task):
    print("to exit type 'exit' ")
    while True:
        a = input("\rEnter Task: ")
        if a == 'exit':
            print("---------------------\n")
            return task
        task.append(a)

todo()
task = []
while True:
    print("1. View Task\n2. Add Task\n4. Exit")
    choice = int(input("Enter the corresponding number to select: "))
    print("\r")

    if choice == 1:
        show(task)
    elif choice == 2:
        add(task)
    elif choice == 4:
        print("Thanks Buddy")
        break


