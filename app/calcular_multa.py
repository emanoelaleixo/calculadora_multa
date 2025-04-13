import tkinter as tk
from tkinter import messagebox

def formatar_moeda_brasileira(event):
    texto = entry_valor.get()
    texto = ''.join(filter(str.isdigit, texto))

    if texto:
        valor = int(texto)
        valor_float = valor / 100
        valor_formatado = f"{valor_float:,.2f}".replace(".", "X").replace(",", ".").replace("X", ",")
        entry_valor.delete(0, tk.END)
        entry_valor.insert(0, valor_formatado)

def formatar_valor(valor_str):
    return valor_str.replace(".", "").replace(",", ".")

def calcular():
    try:
        valor_br = entry_valor.get()
        quantidade = entry_quantidade.get()

        valor = float(formatar_valor(valor_br))
        quantidade = int(quantidade)

        total = valor * quantidade
        valor_10 = total * 0.10
        resultado_var.set(f"R$ {valor_10:,.2f}".replace(".", "X").replace(",", ".").replace("X", ","))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos. Exemplo: 1.234,56")

def limpar_campos():
    entry_valor.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    resultado_var.set("")

cor_fundo = "#F4F9F8"
cor_titulo = "#0B3D2E"
cor_label = "#2F4F4F"
cor_botao = "#2AB587"
cor_botao_hover = "#219d74"
cor_texto_botao = "#FFFFFF"
fonte_titulo = ("Inter", 16, "bold")
fonte_label = ("Source Sans Pro", 11)

janela = tk.Tk()
janela.title("Calculadora de 10%")
janela.geometry("400x300")
janela.configure(bg=cor_fundo)
janela.resizable(False, False)

titulo = tk.Label(
    janela,
    text="Calcular Multa de Cancelamento",
    font=fonte_titulo,
    fg=cor_titulo,
    bg=cor_fundo
)
titulo.pack(pady=10)

frame = tk.Frame(janela, bg=cor_fundo)
frame.pack(pady=5)

label_valor = tk.Label(frame, text="Valor de Boleto(R$):", font=fonte_label, fg=cor_label, bg=cor_fundo)
label_valor.grid(row=0, column=0, sticky="e", pady=5)
entry_valor = tk.Entry(frame)
entry_valor.grid(row=0, column=1, pady=5)
entry_valor.bind("<KeyRelease>", formatar_moeda_brasileira)

label_quantidade = tk.Label(frame, text="Qt. de Boletos Restantes:", font=fonte_label, fg=cor_label, bg=cor_fundo)
label_quantidade.grid(row=1, column=0, sticky="e", pady=5)
entry_quantidade = tk.Entry(frame)
entry_quantidade.grid(row=1, column=1, pady=5)

def estilo_botao(widget):
    widget.configure(
        bg=cor_botao,
        fg=cor_texto_botao,
        activebackground=cor_botao_hover,
        activeforeground=cor_texto_botao,
        font=("Segoe UI", 10, "bold"),
        bd=0,
        relief="flat",
        padx=10,
        pady=5,
        cursor="hand2"
    )

def on_enter(e):
    e.widget.configure(bg=cor_botao_hover)

def on_leave(e):
    e.widget.configure(bg=cor_botao)

frame_botoes = tk.Frame(janela, bg=cor_fundo)
frame_botoes.pack(pady=10)

btn_calcular = tk.Button(frame_botoes, text="Calcular", command=calcular)
estilo_botao(btn_calcular)
btn_calcular.grid(row=0, column=0, padx=5)
btn_calcular.bind("<Enter>", on_enter)
btn_calcular.bind("<Leave>", on_leave)

btn_limpar = tk.Button(frame_botoes, text="Limpar", command=limpar_campos)
estilo_botao(btn_limpar)
btn_limpar.grid(row=0, column=1, padx=5)
btn_limpar.bind("<Enter>", on_enter)
btn_limpar.bind("<Leave>", on_leave)

frame_resultado = tk.Frame(janela, bg=cor_fundo)
frame_resultado.pack()

tk.Label(
    frame_resultado,
    text="Valor de Multa:",
    font=fonte_label,
    fg=cor_label,
    bg=cor_fundo
).grid(row=0, column=0, pady=5)

resultado_var = tk.StringVar()
label_resultado = tk.Label(
    frame_resultado,
    textvariable=resultado_var,
    font=("Segoe UI", 12, "bold"),
    fg="#0B3D2E",
    bg=cor_fundo
)
label_resultado.grid(row=0, column=1, pady=5)

janela.mainloop()
