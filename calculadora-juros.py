# Autor: Gabriela Souza
# Calculadora de Juros (Simples e Composto)
# Data de criação: 19/06/2026

from PIL import Image
import customtkinter as ctk

# ========================================== PALHETA DE CORES ==========================================
COR_FUNDO = ('#E4F2ED', '#284C55')
COR_FUNDO_APP = ("#F9FBFC", "#305B66")
COR_BOTAO = ('#43A27D', '#4B9181')
HOVER_BOTAO = ('#4B9181', '#43A27D')
COR_TEXTO = ('#0F0F0F', '#FFFFFF')
COR_TEXTO_SECUNDARIO = ('#4B9181', '#43A27D')

# ===================================== CONFIGURAÇÕES DE APARÊNCIA =====================================
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("500x800")
app.configure(fg_color=COR_FUNDO_APP)
app.title("CALCULADORA DE JUROS")
app.iconbitmap("assets/icons/calculadora.ico")
app.resizable(False,False)

# ========================================== FUNÇÃO DE CÁLCULO ==========================================
def calcular():
    capital = float(entrada_capital.get())
    taxa = float(entrada_taxa.get())
    tempo = int(entrada_tempo.get())

    if tipo_juros == "Juros Simples":
        juros = capital * (taxa/100) * tempo
        montante = capital + juros
    else:
        montante = capital * (1 + taxa/100)**tempo
        juros = montante - capital

    resultado_capital.configure(text=f"Valor inicial (C): R$ {capital:.2f}")
    resultado_juros.configure(text=f"Juros: R$ {juros:.2f}")
    resultado_montante.configure(text=f"Valor Total (M): R$ {montante:.2f}")
    

# =========================================== FUNÇÃO DO BOTÃO ===========================================
tipo_juros = "Juros Simples"
def trocar_tipo():
    global tipo_juros
    if tipo_juros == "Juros Simples":
        tipo_juros = "Juros Composto"
        titulo2.configure(text="Juros Composto")
        botao_tipo.configure(text="Juros Simples")
    else:
        tipo_juros = "Juros Simples"
        titulo2.configure(text="Juros Simples")
        botao_tipo.configure(text="Juros Composto")

# ============================================ FUNÇÃO DO TEMA ============================================
tema = "light"
def mudar_tema():
    global tema
    if tema == "light":
        tema = "dark"
        ctk.set_appearance_mode("dark")
    else:
        tema = "light"
        ctk.set_appearance_mode("light")

# =========================================== IMAGEM DA JANELA ===========================================
imagem = ctk.CTkImage(
    light_image=Image.open("assets/images/calculadora.png"),
    dark_image=Image.open("assets/images/calculadora.png"),
    size=(80,90)
)

# ============================ FRAME CABEÇALHOS ============================
frame_cabecalho = ctk.CTkFrame(app, fg_color=COR_FUNDO_APP)
frame_cabecalho.pack(pady=10, fill="x", padx=10)

icone = ctk.CTkLabel(frame_cabecalho,
                     image=imagem,
                     text="")
icone.pack(side="left", padx=10)

# ============================= FRAME TÍTULOS =============================

frame_titulos = ctk.CTkFrame(frame_cabecalho, fg_color="transparent")
frame_titulos.pack(side="left", padx=10, expand=True, fill="both")

# ============================== FRAME TEMA ==============================
frame_tema = ctk.CTkFrame(frame_cabecalho,
                          fg_color="transparent")
frame_tema.pack(side="right", pady=(0,5), padx=10)


# ======================================== COMPONENTES DA JANELA ========================================
# ============================================== BOTÃO TEMA =============================================
botao_tema = ctk.CTkButton(frame_tema,
                           text="🌙 Tema",
                           font=('Arial', 12, 'bold'),
                           fg_color=COR_FUNDO_APP,
                           border_color=COR_BOTAO,
                           border_width=1.5,
                           text_color=COR_TEXTO,
                           hover_color=HOVER_BOTAO,
                           command=mudar_tema
                           ).pack(pady=(0,5))

# ============================================== CABEÇALHO ==============================================
titulo1 = ctk.CTkLabel(frame_titulos,
                       text="Calculadora de",
                       font=('Arial', 30, 'bold'),
                       text_color=COR_TEXTO)
titulo1.pack(pady=(20, 0), anchor="w")

titulo2 = ctk.CTkLabel(frame_titulos,
                       text=tipo_juros,
                       font=('Arial', 26, 'bold'),
                       text_color=COR_TEXTO_SECUNDARIO)
titulo2.pack(anchor="w")

paragrafo = ctk.CTkLabel(frame_titulos,
                         text="Calcule seus juros de forma rápida e fácil.",
                         font=('Arial', 15),
                         text_color=COR_TEXTO)
paragrafo.pack(pady=(0, 10), anchor="w")

# =========================================== ENTRADA DE DADOS ===========================================
capital_titulo = ctk.CTkLabel(app,
                              text="Capital (R$)",
                              font=('Arial', 15, 'bold'))
capital_titulo.pack(pady=(5,0), padx=50, anchor='w')

entrada_capital = ctk.CTkEntry(app,
                               placeholder_text="Ex.: 1000.00",
                               width=400,
                               height=40,
                               corner_radius=8)
entrada_capital.pack(pady=5)

taxa_titulo = ctk.CTkLabel(app,
                              text="Taxa de juros (%)",
                              font=('Arial', 15, 'bold'))
taxa_titulo.pack(pady=(5,0), padx=50, anchor='w')

entrada_taxa = ctk.CTkEntry(app,
                            placeholder_text="Ex.: 0.8",
                            width=400,
                            height=40,
                            corner_radius=8)
entrada_taxa.pack(pady=5)

tempo_titulo = ctk.CTkLabel(app,
                              text="Tempo (meses)",
                              font=('Arial', 15, 'bold'))
tempo_titulo.pack(pady=(5,0), padx=50, anchor='w')

entrada_tempo = ctk.CTkEntry(app,
                            placeholder_text="Ex.: 12",
                            width=400,
                            height=40,
                            corner_radius=8)
entrada_tempo.pack(pady=5)

# =============================================== BOTÕES ===============================================
botao_tipo = ctk.CTkButton(app,
                           text= "Juros Composto",
                           command=trocar_tipo,
                           fg_color=COR_BOTAO,
                           hover_color=HOVER_BOTAO)
botao_tipo.pack(pady=10)

botao_calcular = ctk.CTkButton(app,
                               text="Calcular",
                               command=calcular,
                               font=('Arial', 15, 'bold'),
                               fg_color=COR_BOTAO,
                               hover_color=HOVER_BOTAO).pack(pady=10)

#============================================== RESULTADOS ==============================================
resultado = ctk.CTkLabel(app,
                         text="Resultados",
                         font=('Arial', 15, 'bold'),
                         text_color=COR_TEXTO)
resultado.pack(pady=(10,5), padx=50, anchor='w')

resultado_capital = ctk.CTkLabel(app,
                                 text="",
                                 font=('Arial', 14, 'bold'),
                                 text_color=COR_TEXTO)
resultado_capital.pack(pady=(0,5))

resultado_juros = ctk.CTkLabel(app,
                               text="",
                               font=('Arial', 14, 'bold'),
                               text_color=COR_TEXTO)
resultado_juros.pack()

resultado_montante = ctk.CTkLabel(app,
                                  text="",
                                  font=('Arial', 14, 'bold'),
                                  text_color=COR_TEXTO)
resultado_montante.pack()

# =============================================== FÓRMULAS ===============================================
base_calculo = ctk.CTkLabel(app,
                            text=" Fórmulas utilizadas: J = C x i x t | M = C + J",
                            font=('Arial', 12),
                            text_color=COR_TEXTO)
base_calculo.pack(side='bottom')

# ============================================= INICIALIZAÇÃO =============================================
app.mainloop()