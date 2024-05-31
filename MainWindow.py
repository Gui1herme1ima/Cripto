import customtkinter as ctk
from PIL import Image, ImageTk
import os

# Função para centralizar a janela
def centralizar_janela(root, largura, altura):
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    x = (largura_tela / 2) - (largura / 2)
    y = (altura_tela / 2) - (altura / 2)
    root.geometry('%dx%d+%d+%d' % (largura, altura, x, y))

# Função para carregar a imagem
def carregar_imagem(caminho, tamanho):
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    imagem = Image.open(caminho)
    imagem = imagem.resize(tamanho, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(imagem)

# Configurações iniciais
ctk.set_appearance_mode("system")  # Define o modo de aparência para seguir o tema do sistema operacional
ctk.set_default_color_theme("blue")  # Define o tema de cores padrão

# Criação da janela principal
root = ctk.CTk()
root.title("Criptografia")

# Define o tamanho da janela
largura_janela = 800
altura_janela = 400

# Centraliza a janela na tela
centralizar_janela(root, largura_janela, altura_janela)

# Carrega as imagens (os caminhos devem ser atualizados para onde suas imagens estão)
icone_cripto = carregar_imagem("img/CriptoButton.png", (146, 80))  # Exemplo de caminho
icone_copiar = carregar_imagem("img/Copy.png", (20, 20))  # Exemplo de caminho

# Layout da interface
frame_principal = ctk.CTkFrame(root)
frame_principal.pack(padx=20, pady=20, fill="both", expand=True)

# Texto de entrada
label_texto = ctk.CTkLabel(frame_principal, text="Digite o que deseja criptografar:", anchor="w")
label_texto.grid(row=0, column=0, sticky="w", padx=10, pady=5)

entry_texto = ctk.CTkEntry(frame_principal, width=500, height=40)
entry_texto.grid(row=1, column=0, padx=10, pady=5, columnspan=2, sticky="w")

# Botão de Criptografia
botao_cripto = ctk.CTkButton(frame_principal,text="", image=icone_cripto, compound="right")
botao_cripto.grid(row=1, column=2, padx=10, pady=5, sticky="e")

# Resultado da criptografia
label_cripto = ctk.CTkLabel(frame_principal, text="Entrada Criptografada:", anchor="w")
label_cripto.grid(row=2, column=0, sticky="w", padx=10, pady=5)

entry_cripto = ctk.CTkEntry(frame_principal, width=500, height=40)
entry_cripto.grid(row=3, column=0, padx=10, pady=5, columnspan=2, sticky="w")

botao_copiar_cripto = ctk.CTkButton(frame_principal, image=icone_copiar, text="", width=40, height=40)
botao_copiar_cripto.grid(row=3, column=2, padx=10, pady=5, sticky="e")

# Chave de criptografia
label_key = ctk.CTkLabel(frame_principal, text="Cripto Key:", anchor="w")
label_key.grid(row=4, column=1, sticky="e", padx=10, pady=5)

entry_key = ctk.CTkEntry(frame_principal, width=100, height=40)
entry_key.grid(row=4, column=2, padx=10, pady=5, sticky="w")

botao_copiar_key = ctk.CTkButton(frame_principal, image=icone_copiar, text="", width=40, height=40)
botao_copiar_key.grid(row=4, column=3, padx=10, pady=5, sticky="w")

# Inicia o loop principal da interface gráfica
root.mainloop()