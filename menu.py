from tkinter import messagebox
from crypt import *


class MainMenu:

    def __init__(self, app_name):
        self.app_name = app_name

    def quit_app(self):
        self.app_name.quit()

    @staticmethod
    def show_about(event=None):
        messagebox.showwarning(
            "About",
            "MalzaCrypt v0.1"
        )

    def main_wrapper(self):
        the_menu = Menu(self.app_name)

        file_menu = Menu(the_menu, tearoff=0)

        file_menu.add_command(label="Generate Key", command=key_generator)
        file_menu.add_separator()
        file_menu.add_command(label="Encrypt", command=encrypt)
        file_menu.add_separator()
        file_menu.add_command(label="Decrypt", command=decrypt)
        file_menu.add_separator()
        file_menu.add_command(label="About", command=self.show_about)

        the_menu.add_cascade(label="File", menu=file_menu)
        self.app_name.config(menu=the_menu)
