import datetime
from todo import Todo
todo=Todo()

# App Welcome 
print("==========================\n")
print("|   Welcome To Todo App  |\n")
print("==========================\n")

# App FunctionalitiesOptions
def printOptions():
    print("1.Create Todo")
    print("2.Print All Todos")
    print("3.Get Single Todo")
    print("4.Update A Todo")
    print("5.Delete Todo")
    print("6.Delete All Todos")
    print("7.Show Menu")
    print("8.Exit\n")
printOptions()


# App Engine
def todoEngine():
    running = True
    while running:
        options = input("Enter a option : ")
        match options:
            case '1':
                todo.createTodo()
            case '2':
                todo.printAllTodos()
            case '3':
                todo.getATodo()
            case '4':
                todo.updateTodo()
            case '5':
                todo.deleteTodo()
            case '6':
                todo.deleteAllTodo()
            case '7':
                printOptions()
            case '8':
                print("Thanks For Using This Todo App:)")
                running=False
            case _:
                print("Please Provide a valid Option\n")
                printOptions()

    
todoEngine()