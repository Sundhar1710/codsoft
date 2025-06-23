def todo():
    print("Welcome to To-Do List App")

def show(task):
    if not task:
        print("No Task to View...")
    for i in task:
        print(f"{i}\r")
    print("---------------------\n")

def add(task):
    print("To EXIT type 'exit' ")
    while True:
        a = input("\rEnter Task: ")
        if a == 'exit':
            print("---------------------\n")
            return task
        task.append(a)

def modify(task):
    if not task:
        print("No Task to Modify...")
        print("---------------------\n")
        return
    print("Current Task are below\r")
    print("---------------------\r")
    for i, t in enumerate(task,start = 1):
        print(f"{i}. {t}\r")
    c = int(input("Enter corresponding Number to Modify: "))
    c = c - 1
    if 0 <= c <= len(task):
        print(f"You select '{task[c]}' to Modify.")
        chan = input("Enter the Modification: ")
        print(f"Modification Successful {task[c]} ---> {chan}")
        task[c] = chan
        print("---------------------\n")
        return task

def delete(task):
    if not task:
        print("No Task to Delete....")
        print("---------------------\n")
        return
    print("---------------------\r")
    print("Current Task are below\r")
    for i, t in enumerate(task, start = 1):
        print(f"{i}. {t}\r")
    d = int(input("Enter corresponding Number to Delete: "))
    if task[d-1] in task:
        task.remove(task[d-1])
        print("---------------------\r")
        print("Task Deleted successfully\r")
        print("---------------------\n")
        return task
    else:
        print("No such Number!")
        print("---------------------\n")
    
todo()
task = []
while True:
    print("1. View Task\n2. Add Task\n3. Modify Task\n4. Delete Task\n5. Exit")
    choice = int(input("Enter the corresponding number to select: "))
    print("\r")

    if choice == 1:
        show(task)
    elif choice == 2:
        add(task)
    elif choice == 3:
        modify(task)
    elif choice == 4:
        delete(task)
    elif choice == 5:
        print("Thanks Buddy")
        print("---------------------\r")
        break


