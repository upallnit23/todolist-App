todolist = []
#Function prints title and menu list for to-do list
def titlescreen():
    print("Welcome to the To-Do-List App!\n")
    print("Please look at the menu below.\n")
    print("Menu: \n")
    print("1. Add a task \n")
    print("2. View tasks \n")
    print("3. Mark a task as complete \n")
    print("4. Delete a task \n")
    #print("5. Quit \n")
    #menuselect = int(input("Please select a number from the menu above. "))
    #return menuselect

#This function selects menu choice for to-do list
"""def menuselection():
    menuselect = int(input("Please select a number from the menu above. "))
    if menuselect == 1:
        tasktoperform()
    if menuselect == 2:
        printlist(todolist)
    if menuselect == 3:
        completedtasks(todolist)
    if menuselect == 4:
        completedtasks(todolist)
    if menuselect == 5:
        quitit()
    else:
        return menuselect """

#Function to pick tasks to do and format output of to-do list.    
def tasktoperform():
    todolist = []
    task = ""
    while task != "end":

        print("Which task do you want to perform? ")
        print("a - meal prep and cooking meals, ")
        print("b - cleaning rooms in house ")
        print("c - laundry ")
        print("d - homework completion")
        print("e - feeding and walking pets ")
        print("f - lawn and/or plant care ")
        print("g - meditation time ")
        print("h - exercise and sports for family ")

        choice = input("Enter a letter for the task to complete: ")
        if choice == "end":
            print(todolist)
            break
        if choice == "a":
            todolist.append("Prep and cook meals. \n")
        elif choice == "b":
            todolist.append("Clean rooms. \n")
        elif choice == "c":
            todolist.append("Do laundry. \n")
        elif choice == "d":
            todolist.append("Finish homework. \n")
        elif choice == "e":
            todolist.append("Feed and walk pets. \n")
        elif choice == "f":
            todolist.append("Check plants and lawn. \n")
        elif choice == 'g':
            todolist.append("Personal time. \n")
        elif choice == 'h':
            todolist.append("Workout. \n")
        #elif choice in 'abcdefgh':
        #    todolist.append(gettasklist(todolist))
        elif choice >= 'h':
            print("Invalid choice.  Choose again. ")
            choice = input("Enter a letter for the task to complete: ")
    #choice = input("Enter a letter for the task to complete: ")

    return todolist

#This function gets the printed list
"""def gettasklist(choice):
    if choice == "a":
        todolist.append("Prep and cook meals. \n")
    elif choice == "b":
        todolist.append("Clean rooms. \n")
    elif choice == "c":
        todolist.append("Do laundry. \n")
    elif choice == "d":
        todolist.append("Finish homework. \n")
    elif choice == "e":
        todolist.append("Feed and walk pets. \n")
    elif choice == "f":
        todolist.append("Check plants and lawn. \n")
    elif choice == 'g':
        todolist.append("Personal time. \n")
    elif choice == 'h':
        todolist.append("Workout. \n")
    else:
        print("Invalid choice.")
    """
    

#Function prints to-do list
def printlist(updatedlist):
    for task in updatedlist:
        print(updatedlist)

#This function marks tasks as completed
def completedtasks(todolist):
    ctask = []
    dtask = int(input("Enter task to delete, or 0 to end program: "))
    while dtask != 0:
        dtask = int(input("Enter the task completed, or 0 to end program: "))
        if dtask == 0:
            break
        try:
            dtask = int(dtask)
            if dtask <= 0 or dtask > len(todolist):
                print("Invalid number. ")
            else:
                ctask.append(dtask)
                todolist.pop(dtask-1)
        except ValueError as e:
            print(e)
        except IndexError as e:
            print(e)
    print(f"This is the updated to-do list: {todolist}.")
    print(f"These are the tasks completed and removed from the list: {ctask}.")


#This function gives an exit statement for the to-do list application.
def quitit():
    print("Thank you for using the to-do list app. ")
#Main program

titlescreen()
menuselect = int(input("Please select a number from the menu above. "))
try:
    if menuselect == 1:
        tasktoperform()
    if menuselect == 2:
        printlist(todolist)
    if menuselect == 3:
        completedtasks(todolist)
    if menuselect == 4:
        completedtasks(todolist)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    quitit()
    
