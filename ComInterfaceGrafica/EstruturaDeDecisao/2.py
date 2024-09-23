import tkinter as tk
from tkinter import messagebox

def verificar_numero():
    num1 = float(entry_num1.get())
    if num1 < 0:
        messagebox.showinfo("Resultado", f'O número {num1} é negativo')
    else:
        messagebox.showinfo("Resultado", f'O número {num1} é positivo')

# Criando a janela
janela = tk.Tk()
janela.title("Verificador de Número")

# Entrada
label_num1 = tk.Label(janela, text="Insira o número:")
label_num1.pack()
entry_num1 = tk.Entry(janela)
entry_num1.pack()

# Botão
botao_verificar = tk.Button(janela, text="Verificar", command=verificar_numero)
botao_verificar.pack()

# Iniciar a interface
janela.mainloop()
