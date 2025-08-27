import datetime

class Todo:
    def __init__(self):
        print("Todo cleass")
    def getData(self):
        '''return all todos'''
        try:
            with open("data.txt","r") as file:
                todos = file.readlines()
                if not todos:
                    print("Todos not created Yet.")
                else:
                    return todos
        except FileNotFoundError:
            print("Todos not creates yet.")
    def createTodo(self):
        todo = input("Enter Todo : ")
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open("data.txt","r") as file:
                lines = file.readlines()
                todoId = len(lines) + 1
        except FileNotFoundError:
            todoId = 1
        with open("data.txt","a") as file:
            file.write(f"{todoId} | {todo} | {date}\n")
            print("Todo Created Successfully.")
    def printSingleTodo(self,line):
        '''print single todo '''
        todoId,todo,date=line.strip().split("|")
        print(f"{todoId}. {todo}\nCreation Date : {date}\n")
    def printAllTodos(self):
        todos = self.getData()
        if not todos: return
        for line in todos:
            self.printSingleTodo(line)
    def getATodo(self):
        todoId = int(input("Enter Todo Id : "))
        todos = self.getData()
        if not todos: return
        elif 0 >= todoId or todoId > len(todos):
            print("Id is Not Valid")
            return
        todoId,todo,date=todos[todoId-1].strip().split("|")
        print(f"{todoId}. {todo}\nCreation Date : {date}\n")
    def updateTodo(self):
        todos = self.getData()
        todoId = int(input("Enter Todo Id : "))
        if not todos: return
        elif 0 >= todoId or todoId > len(todos):
            print("Id is Not Valid")
            return
        updatedData = input("Enter Todo for Update : ")
        todos[todoId-1] = f"{todoId} | {updatedData} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        with open("data.txt","w") as file:
            for line in todos:
                file.writelines(line)
        print("Todo Update Successfully:)")
    def deleteTodo(self):
        todos = self.getData()
        todoId = int(input("Enter Todo Id for Delete : "))
        if not todos: return
        elif 0 >= todoId or todoId > len(todos):
            print("Id is Not Valid")
            return
        todos.pop(todoId-1)
        with open("data.txt","w") as file:
            for line in todos:
                file.write(line)
        print("Todo Deleted Successfully:)")
    def deleteAllTodo(self):
        with open("data.txt","w") as file:
            file.write("")
        print("All todos Are Deleted Successfully:)")
        




