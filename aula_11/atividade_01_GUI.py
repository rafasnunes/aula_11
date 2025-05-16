# Criar um programa que peça duas notas ao usuário, calcule a média e informe
# se o = aluno foi aprovado. O programa deve:
# 1. Usar try para converter as notas para float.
# 2. Usar except para tratar erro caso o usuário digite texto/valor inválido.
# 3. Usar else (caso não dê erro no try) para: o Verificar se as notas estão
# no intervalo de 0 a 10.
# 4. Calcular e exibir a média.
# 5. Informar se o aluno foi aprovado (média ≥ 6).
# 6. Usar finally para exibir uma mensagem de encerramento do programa.

# Aplicação do programa com interface gráfica ( GUI )

import tkinter as tk
from tkinter import messagebox

def calcular_media():

    try:
        n1 = float(entry_nota1.get())
        n2 = float(entry_nota2.get())
    
    except ValueError:
        messagebox.showerror("Erro de entrada", "Digite apenas números válidos.")
    
    else:
    
        if 0 <= n1 <= 10 and 0 <= n2 <= 10:
            media = (n1 + n2) / 2
            resultado = f"Média: {media:.2f}\n"
    
            if media >= 6:
                resultado += "Aluno aprovado!"
    
            else:
                resultado += "Aluno reprovado."
            messagebox.showinfo("Resultado", resultado)
    
        else:
            messagebox.showwarning("Valor inválido", "As notas devem estar entre 0 e 10.")
    
    finally:
        print("Obrigado por utilizar o programa.")  # Console log

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculador de Médias")
janela.geometry("300x200")

# Widgets
tk.Label(janela, text="Digite a primeira nota:").pack(pady=5)
entry_nota1 = tk.Entry(janela)
entry_nota1.pack()

tk.Label(janela, text="Digite a segunda nota:").pack(pady=5)
entry_nota2 = tk.Entry(janela)
entry_nota2.pack()

tk.Button(janela, text="Calcular Média", command=calcular_media).pack(pady=10)

# Iniciar o loop da interface
janela.mainloop()
