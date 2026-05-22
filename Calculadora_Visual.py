import customtkinter as ctk


ctk.set_appearance_mode("light")  # Modos: "light", "dark", "system"
ctk.set_default_color_theme("green")  # Temas: "blue", "green", "dark-blue"
ctk.set_widget_scaling(0.5)  # dimensões dos elementos em relação a janela
ctk.set_window_scaling(2.0)  # dimensões da janela

app = ctk.CTk()
app.geometry("300x400")
app.title("Calculadora de Juros")
app.iconbitmap("assets/ico/calculadora.ico")
app.resizable(False, False) # impedir que o usuário redimensione a janela

# Lógica da calculadora

# Configurações dos elementos da interface
# Titulo da calculadora
label_title = ctk.CTkLabel(app, 
                           text="Calculadora",
                           font=('Arial', 50, 'bold'),
                           text_color="#0F0F0F",
                           )
label_title.pack(pady=(40, 0))

label_title2 = ctk.CTkLabel(app,
                            text="Juros Simples",
                            font=('Arial', 40, 'bold'),
                            text_color="#43A27D")
label_title2.pack(pady=(0, 30))

# Elementos de entrada de dados
# Valor Inicial
valorInicial_label = ctk.CTkLabel(app, 
                                  text="Valor Inicial", 
                                  font=('Arial', 30),
                                  text_color="#0F0F0F",)
valorInicial_label.pack(pady=20)

valorInicial_entry = ctk.CTkEntry(app,
                                  placeholder_text="R$ 0,00",
                                  font=('Arial', 30),
                                  width=250,
                                  height=50,
                                  )
valorInicial_entry.pack(pady=20)

# Taxa de Juros
taxaJuros_label = ctk.CTkLabel(app,
                               text="Taxa de Juros (%)",
                               font=('Arial', 30),
                               text_color="#0F0F0F")
taxaJuros_label.pack(pady=20)

taxaJuros_entry = ctk.CTkEntry(app,
                               placeholder_text="0,00",
                               font=('Arial', 30),
                               width=250,
                               height=50)
taxaJuros_entry.pack(pady=20)

# Período
periodo_label = ctk.CTkLabel(app,
                            text="Período (meses)",
                            font=('Arial', 30),
                            text_color="#0F0F0F")
periodo_label.pack(pady=20)

periodo_entry = ctk.CTkEntry(app,
                            placeholder_text="0",
                            font=('Arial', 30),
                            width=250,
                            height=50)
periodo_entry.pack(pady=20)

# Botão de calcular
botao = ctk.CTkButton(app,
                        text="Calcular",
                        command=lambda: print("Calculando..."),
                        corner_radius= 10,
                        fg_color="#43A27D",
                        hover_color="#4B9181",
                        font=('Arial', 30, 'bold'),
                        width=200,
                        height=50)
botao.pack(pady=30)

# Resultado
resultado_label = ctk.CTkLabel(app,
                               text="Resultados",
                               font=('Arial', 30, 'bold'),
                               text_color="#43A27D")
resultado_label.pack(pady=20)

resultado = ctk.CTkLabel(app,
                         text="Valor Final: R$ 0,00\nJuros: R$ 0,00",
                         font=('Arial', 30),
                        text_color="#0F0F0F")
resultado.pack(pady=20)



app.mainloop()