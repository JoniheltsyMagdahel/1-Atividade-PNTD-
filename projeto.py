import tkinter as tk
from tkinter import messagebox

def mostrar_mensagem():
    messagebox.showinfo("Mensagem", "Você clicou no botão!")

janela = tk.Tk()
janela.title("Interface Gráfica")
janela.geometry("800x400")

rotulo = tk.Label(janela, text="Vai dar bom")
rotulo.pack()

botao = tk.Button(janela, text="Clique aqui", command=mostrar_mensagem)
botao.pack()

janela.mainloop()