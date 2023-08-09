import os
import shutil
import tkinter as tk
from tkinter import filedialog


def organizar_arquivos():
    diretorio_origem = filedialog.askdirectory()
    # Solicitar ao usuário que escolha a pasta

    if diretorio_origem:
        for nome_arquivo in os.listdir(diretorio_origem):
            if os.path.isfile(os.path.join(diretorio_origem, nome_arquivo)):
                extensao = nome_arquivo.split(".")[-1]
                pasta_destino = os.path.join
                (diretorio_origem, extensao.upper())

                if not os.path.exists(pasta_destino):
                    os.mkdir(pasta_destino)

                caminho_arquivo_origem = os.path.join
                (diretorio_origem, nome_arquivo)

                caminho_arquivo_destino = os.path.join
                (pasta_destino, nome_arquivo)

                shutil.move(caminho_arquivo_origem, caminho_arquivo_destino)


app = tk.Tk()
app.title("Organizador de Arquivos")

btn_organizar = tk.Button(app,
                          text="Organizar Arquivos",
                          command=organizar_arquivos)
btn_organizar.pack(padx=20, pady=20)

app.mainloop()

