import tkinter as tk
from tkinter import messagebox

def comparar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if num1 > num2:
        messagebox.showinfo("Resultado", f'O número {num1} é maior que {num2}')
    else:
        messagebox.showinfo("Resultado", f'O número {num2} é maior que {num1}')

# Criando a janela
janela = tk.Tk()
janela.title("Comparador de Números")

# Entradas
label_num1 = tk.Label(janela, text="Insira o primeiro número:")
label_num1.pack()
entry_num1 = tk.Entry(janela)
entry_num1.pack()

label_num2 = tk.Label(janela, text="Insira o segundo número:")
label_num2.pack()
entry_num2 = tk.Entry(janela)
entry_num2.pack()

# Botão
botao_comparar = tk.Button(janela, text="Comparar", command=comparar)
botao_comparar.pack()

# Iniciar a interface
janela.mainloop()
