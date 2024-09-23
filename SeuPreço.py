import tkinter as tk
from tkinter import messagebox

# Funções do algoritmo
def calcular_preco_ideal(preco_fornecedor, frete_fornecedor):
    morcap = preco_fornecedor * 2.5
    taxa_mercado_pago = (morcap * 5) / 100
    preco_total_fornecedor = morcap + frete_fornecedor
    preco_para_venda = preco_total_fornecedor + taxa_mercado_pago
    imposto_lucro_bruto = (preco_para_venda * 15) / 100
    preco_ideal_venda = imposto_lucro_bruto + preco_para_venda
    preco_ideal_dolar = preco_ideal_venda * 6
    return preco_ideal_venda, preco_ideal_dolar

def calcular_projecao_lucro(preco_ideal_venda, qntd_vendas):
    lucro_diario = qntd_vendas * preco_ideal_venda
    lucro_semanal = lucro_diario * 7
    lucro_mensal = lucro_diario * 30
    lucro_bimestral = lucro_diario * 60
    return lucro_diario, lucro_semanal, lucro_mensal, lucro_bimestral

# Função para o botão de cálculo
def calcular():
    try:
        preco_fornecedor = float(entry_preco.get())
        frete_fornecedor = float(entry_frete.get())
        qntd_vendas = int(entry_vendas.get())

        preco_ideal_venda, preco_ideal_dolar = calcular_preco_ideal(preco_fornecedor, frete_fornecedor)
        lucro_diario, lucro_semanal, lucro_mensal, lucro_bimestral = calcular_projecao_lucro(preco_ideal_venda, qntd_vendas)
        
        # Exibindo resultados
        result_preco['text'] = f'Preço ideal de venda: R$ {preco_ideal_venda:.2f} | Preço em dólar: $ {preco_ideal_dolar:.2f}'
        result_lucro['text'] = f'Lucro Diário: R$ {lucro_diario:.2f} | Semanal: R$ {lucro_semanal:.2f} | Mensal: R$ {lucro_mensal:.2f} | Bimestral: R$ {lucro_bimestral:.2f}'
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criando a janela
janela = tk.Tk()
janela.title("Calculadora de Preço Ideal")

# Widgets de entrada
tk.Label(janela, text="Preço do Fornecedor:").grid(row=0, column=0, padx=10, pady=5)
entry_preco = tk.Entry(janela)
entry_preco.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Frete do Fornecedor:").grid(row=1, column=0, padx=10, pady=5)
entry_frete = tk.Entry(janela)
entry_frete.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Quantidade de Vendas:").grid(row=2, column=0, padx=10, pady=5)
entry_vendas = tk.Entry(janela)
entry_vendas.grid(row=2, column=1, padx=10, pady=5)

# Botão para calcular
botao_calcular = tk.Button(janela, text="Calcular", command=calcular)
botao_calcular.grid(row=3, column=0, columnspan=2, pady=10)

# Resultados
result_preco = tk.Label(janela, text="")
result_preco.grid(row=4, column=0, columnspan=2)

result_lucro = tk.Label(janela, text="")
result_lucro.grid(row=5, column=0, columnspan=2)

# Iniciando a janela
janela.mainloop()
