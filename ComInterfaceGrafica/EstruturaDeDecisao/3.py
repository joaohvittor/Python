import tkinter as tk
from tkinter import messagebox

def verificar_sexo():
    sexo = entry_sexo.get().upper()
    if sexo == 'M':
        messagebox.showinfo("Resultado", "Sexo Masculino.")
    elif sexo == 'F':
        messagebox.showinfo("Resultado", "Sexo Feminino.")
    else:
        messagebox.showwarning("Erro", "Sexo Inválido.")

# Criando a janela
janela = tk.Tk()
janela.title("Verificador de Sexo")

# Entrada
label_sexo = tk.Label(janela, text="Digite F ou M:")
label_sexo.pack()
entry_sexo = tk.Entry(janela)
entry_sexo.pack()

# Botão
botao_verificar = tk.Button(janela, text="Verificar", command=verificar_sexo)
botao_verificar.pack()

# Iniciar a interface
janela.mainloop()
