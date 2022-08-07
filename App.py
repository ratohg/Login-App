from tkinter import *
from Database import DataBase
from Animation import Animation
from threading import Thread


class App:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x400")
        self.info_name = Label(self.root, text="Name:")
        self.info_name.place(x=60, y=170)
        self.entry_name = Entry(self.root, width=30)
        self.entry_name.place(x=100, y=170)
        self.info_password = Label(self.root, text="Passwoord:")
        self.info_password.place(x=35, y=200)
        self.entry_password = Entry(self.root, width=30)
        self.entry_password.place(x=100, y=200)
        self.button_login = Button(self.root, text="Login", command=self.login)
        self.button_login.place(x=350, y=370)
        self.button_register = Button(self.root, text="Register", command=self.register)
        self.button_register.place(x=8, y=370)
        self.root.mainloop()
    def get_name_password(self):
        name = self.entry_name.get()
        password = self.entry_password.get()
        return name, password
    def login(self):
        name, password = self.get_name_password()
        user, id = App.check_user(name, password)
        if user == None:
            self.info(f"Usuário {name} não existe ou as credencias estão incorretas", "red")
            return
        print(f"{name} logado com sucesso")
        canvas = Animation(self.root)
        canvas.ball()
        Thread(target=canvas.animation_ball).start()
        Thread(target=canvas.animation_text).start()
        Thread(target=self.stop_animation_run_text, args=(canvas, id,)).start()
        self.entry_name.delete(0, END)
        self.entry_password.delete(0, END)
    def stop_animation_run_text(self, canvas, id):
        canvas.stop_animation()
        App.text_window(self.root, id)
    def register(self):
        name, password = self.get_name_password()
        user, id = App.check_user(name, password)
        if user:
            self.info(f"Usuário {name} já existe", "orange")
            return
        db.edit(f"insert into peoples values (default, '{name}', '{password}', default);")
        self.info(f"Usuário {name} criado", "green")
    def info(self, information, color):
        self.destroy_last_label()
        info_label = Label(self.root, text=information, foreground=color)
        info_label.place(anchor=CENTER, y=250, x=180)
    def destroy_last_label(self):
        last_widget = self.root.winfo_children()[-1]
        if "label" in str(last_widget):
            last_widget.destroy()

    @classmethod
    def text_window(cls, root, id):
        cls.frame = Frame(root, width=400, height=400, background="grey")
        cls.frame.place(x=0, y=0)
        cls.button_logout = Button(cls.frame, text="Logout", command=cls.frame.destroy)
        cls.button_logout.place(x=340, y=5)
        cls.text = Text(cls.frame, width=48, height=22)
        cls.text.place(x=5, y=35)
        cls.button_save = Button(cls.frame, text="Save", command=cls.text_edit)
        cls.button_save.place(x=300, y=5)
        cls.id = id
        cls.last_text()
    @classmethod
    def text_edit(cls):
        content = cls.text.get(1.0, END)
        db.edit(command=f"update peoples set text = '{content}' where id = '{cls.id}'")
    @classmethod
    def last_text(cls):
        last_content = cls.check_user(id=cls.id)
        print(last_content)
        if last_content:
            cls.text.insert(END, last_content)
    @classmethod
    def check_user(self, name="", password="", id=False):
        rows = db.read("select * from peoples;")
        for row in rows:
            if id == row[0]:
                return row[3]
            if name == str(row[1]) and password == str(row[2]):
                return True, row[0]
        return None, None
        

db = DataBase(host="localhost", user="root", password="94945049", database="logins")
db.connect()
App()
db.disconnect()
