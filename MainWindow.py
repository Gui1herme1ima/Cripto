import customtkinter as ctk
import os
import sys

def centralizar_janela(root, largura, altura):
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    x = (largura_tela / 2) - (largura / 2)
    y = (altura_tela / 2) - (altura / 2)
    root.geometry('%dx%d+%d+%d' % (largura, altura, x, y))

root = ctk.CTk()
root.title("Cripto")

largura_janela = 800
altura_janela = 400

centralizar_janela(root, largura_janela, altura_janela)

label = ctk.CTkLabel(root, text="Olá, mundo!", font=("Arial", 24))
label.pack(pady=20)

button = ctk.CTkButton(root, text="Clique Aqui")
button.pack(pady=20)

root.mainloop()