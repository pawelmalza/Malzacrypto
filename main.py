from tkinter import ttk
from menu import *
from crypt import *

root = Tk()

root.geometry("250x500")

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 0.6)

root.geometry("+{}+{}".format(positionRight, positionDown))

root.style = ttk.Style()
root.style.theme_use("aqua")

Label(root, text="MalzaCrypt", height=3, font=("Times", 24)).grid(row=0)

generator = Button(root, text="Generate Key", command=key_generator, width=20, height=3).grid(row=2, pady=10, padx=30)
encrypt_file = Button(root, text="Encrypt File", command=encrypt, width=20, height=3).grid(row=3, pady=10)
decrypt_file = Button(root, text="Decrypt File", command=decrypt, width=20, height=3).grid(row=4, pady=10)
Frame(root, height=50).grid()
quit = Button(root, text="Quit", command=root.quit, width=20, height=3).grid(row=6, pady=20)

MainMenu(root).main_wrapper()

root.mainloop()
