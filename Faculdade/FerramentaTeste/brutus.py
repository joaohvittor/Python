import tkinter as tk
from tkinter import messagebox
import instaloader

def baixar_perfil():
    perfil = entry_perfil.get()
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if not perfil:
        messagebox.showwarning("Erro", "Por favor, insira o nome do perfil.")
        return
    
    loader = instaloader.Instaloader()
    if usuario and senha:
        try:
            loader.login(usuario, senha)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha no login: {e}")
            return
    
    try:
        loader.download_profile(perfil, profile_pic_only=False)
        messagebox.showinfo("Sucesso", f"Download do perfil '{perfil}' concluído.")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha no download: {e}")

# Criar janela principal
janela = tk.Tk()
janela.title("Instaloader Interface")
janela.geometry("400x200")

# Elementos da interface
label_perfil = tk.Label(janela, text="Perfil do Instagram:")
label_perfil.pack()
entry_perfil = tk.Entry(janela)
entry_perfil.pack()

label_usuario = tk.Label(janela, text="Usuário (opcional):")
label_usuario.pack()
entry_usuario = tk.Entry(janela)
entry_usuario.pack()

label_senha = tk.Label(janela, text="Senha (opcional):")
label_senha.pack()
entry_senha = tk.Entry(janela, show="*")
entry_senha.pack()

btn_baixar = tk.Button(janela, text="Baixar Perfil", command=baixar_perfil)
btn_baixar.pack()

# Executar janela
janela.mainloop()
