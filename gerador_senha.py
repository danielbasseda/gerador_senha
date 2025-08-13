import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip  # pip install pyperclip

# Função para gerar a senha
def gerar_senha(tamanho):
    if tamanho < 4:
        messagebox.showerror("Erro", "A senha deve ter pelo menos 4 caracteres!")
        return None
    
    senha = [
        random.choice(string.ascii_letters),
        random.choice(string.punctuation),
        random.choice(string.digits)
    ]
    
    possibilidades = string.ascii_letters + string.digits + string.punctuation
    senha.extend(random.choices(possibilidades, k=tamanho - 3))
    random.shuffle(senha)
    return "".join(senha)

# Função ao clicar em "Gerar Senha"
def gerar_e_mostrar():
    tamanho = slider.get()
    senha = gerar_senha(tamanho)
    if senha:
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)

# Função para copiar senha
def copiar_senha():
    senha = entry_senha.get()
    if senha:
        pyperclip.copy(senha)
        messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")
    else:
        messagebox.showwarning("Aviso", "Nenhuma senha para copiar.")

# Criando a janela principal
root = tk.Tk()
root.title("Gerador de Senhas")
root.geometry("400x250")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Escolha o tamanho da senha:", font=("Arial", 10, "bold")).pack(pady=10)
slider = tk.Scale(root, from_=4, to=100, orient="horizontal", length=250)
slider.set(12)
slider.pack()

tk.Button(root, text="Gerar Senha", font=("Arial", 10, "bold"), command=gerar_e_mostrar).pack(pady=10)

entry_senha = tk.Entry(root, width=35, font=("Arial", 12))
entry_senha.pack(pady=5)

tk.Button(root, text="Copiar Senha", font=("Arial", 10), command=copiar_senha).pack(pady=5)

# Rodar o app
root.mainloop()
