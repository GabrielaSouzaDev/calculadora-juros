# Autor: Gabriela Souza
# Projeto: Calculadora Simples
# Data: 2026-05-23

from pydoc import text

import customtkinter as ctk

# Configuracões da janela
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')
ctk.set_widget_scaling(0.5)
ctk.set_window_scaling(2.0)

app = ctk.CTk()
app.geometry('300x400')
app.title('Calculadora de Juros Composto')
app.iconbitmap('assets/ico/calculadora.ico')
app.resizable(False, False)

# Lógica da Calculadora
def jurosComposto():
    valorInvestido = float(entrada_valorInicial.get())
    taxaJuros = float(entrada_taxaJuros.get())
    # valorMensal = float(entrada_valorMensal.get())
    periodo = int(entrada_periodo.get())

    valorFinal = valorInvestido * (1 + (taxaJuros/100)) ** periodo
    juros = valorFinal - valorInvestido

    resultado.configure(text=(
        f'Valor Investido: R${valorInvestido:.2f}\n'
        f'Juros: R${juros:.2f}\n'
        f'Valor Final: R${valorFinal:.2f}'
    ))

# Configurações dos elementos da interface
titulo1 = ctk.CTkLabel(app,
                       text="Calculadora",
                       font=('Arial', 50, 'bold'),
                       text_color='#FFFFFF')
titulo1.pack(pady=(40, 0))

titulo2 = ctk.CTkLabel(app,
                  text="Juros Composto",
                  font=('Arial', 30, 'bold'),
                  text_color="#1650E2",)
titulo2.pack(pady=(40, 0))

valorInicial_titulo = ctk.CTkLabel(app,
                                    text="Valor Inicial", 
                                    font=('Arial', 30),
                                    text_color="#FFFFFF")
valorInicial_titulo.pack(pady=20)

entrada_valorInicial = ctk.CTkEntry(app,
                                    placeholder_text="0,00",
                                    font=('Arial', 30),
                                    width=250,
                                    height=50)
entrada_valorInicial.pack(pady=20)

# valorMensal_titulo = ctk.CTkLabel(app,
#                                     text="Valor Mensal",
#                                     font=('Arial', 30),
#                                     text_color='#FFFFFF')
# valorMensal_titulo.pack(pady=20)

# entrada_valorMensal = ctk.CTkEntry(app,
#                                    placeholder_text="0,00",
#                                    font=('Arial', 30),
#                                    width=250,
#                                    height=50)
# entrada_valorMensal.pack(pady=20)


taxaJuros_titulo = ctk.CTkLabel(app,
                                text="Taxa de Juros (%)",
                                font=('Arial', 30),
                                text_color="#FFFFFF")
taxaJuros_titulo.pack(pady=20)

entrada_taxaJuros = ctk.CTkEntry(app,
                                placeholder_text="0,00",
                                font=('Arial', 30),
                                width=250,
                                height=50)
entrada_taxaJuros.pack(pady=20)

periodo_titulo = ctk.CTkLabel(app,
                              text='Periodo (meses)',
                              font=('Arial', 30),
                              text_color='#FFFFFF')
periodo_titulo.pack(pady=20)

entrada_periodo = ctk.CTkEntry(app,
                               placeholder_text='0 meses',
                               font=('Arial', 30),
                               width=250,
                               height=50)
entrada_periodo.pack(pady=20)

botao = ctk.CTkButton(app,
                      text='Calcular',
                      command=jurosComposto,
                      corner_radius= 10,
                      fg_color='#1650E2',
                      hover_color='#0F48D9',
                      font=('Arial', 30, 'bold'),
                      width=200,
                      height=50)
botao.pack(pady=30)

# Resultado
resultado_titulo = ctk.CTkLabel(app,
                               text="Resultados",
                               font=('Arial', 30, 'bold'),
                               text_color="#1650E2")
resultado_titulo.pack(pady=20)

resultado = ctk.CTkLabel(app,
                        text="",
                        font=('Arial', 30, 'bold'),
                        text_color="#FFFFFF")
resultado.pack(pady=20)



app.mainloop()