from tkinter import *
from todos_func import *
from PIL import Image,ImageTk



class Todo(Tk):
    def __init__(self):
        super().__init__()
        # root window setup
        self.color1="#1a1a1a"
        self.color2="#222"
        self.color3="#5c5"
        self.title("Todo App Made with ❤️ By Code.Ide")
        self.config(bg=self.color1)
        self.geometry("400x500")
        self.iconbitmap("./img/icon.ico")
        # self.resizable(False,False)  

        # All images
        self.add_todo_img = ImageTk.PhotoImage(Image.open("./img/add.png").resize((30,30)))      
        self.todosList=["todo1","todo2","todo3","todo4","todo5"]
       
    def topFrame(self):
        todo_input_frame = Frame(self,bg=self.color1,relief="flat")
        todo_input_frame.pack(pady=10)
        todo_entry = Entry(todo_input_frame,font=("Arial",20,"bold"),bg=self.color3,fg="white",bd=0)
        todo_entry.grid(row=0,column=0)
        create_todo_btn = Button(todo_input_frame,image=self.add_todo_img,bg=self.color1,activebackground=self.color1,bd=0,relief="flat",highlightthickness=0,cursor="hand2",command=createTodo)
        create_todo_btn.grid(row=0,column=1,padx=10)
    def bottomFrame(self):
        self.list_frame=Frame(self,bg=self.color2)
        self.list_frame.pack(fill="both",expand=True)
        todo_label = Label(self.list_frame,bg=self.color2,fg="white",font=("Arial",20,"bold"),text="Todo List")
        todo_label.pack()
    def todoListBox(self):
        todo_list_box = Listbox(self.list_frame,bg=self.color2,fg="white",font=("Courier",12),bd=0,highlightthickness=0,relief="flat",width=400,cursor="hand2")
        todo_list_box.pack(pady=10,padx=10)
        for item in self.todosList:
            itemLabel = Label(todo_list_box,text=item)
            itemLabel.pack()
            todo_list_box.insert(END,itemLabel)

        
    def renderUi(self):
        self.topFrame()
        self.bottomFrame()
        self.todoListBox()
      
    def engine(self):
        pass




# code execution
if __name__ == "__main__":
    todo_app = Todo()
    todo_app.renderUi()
    todo_app.mainloop()



