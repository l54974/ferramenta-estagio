import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext
from analyzer import CodeAnalyzer
from generator import gerar_testes
from executor import executar_testes
from utils import nome_sem_extensao
import os

caminho_codigo = ""
funcoes_encontradas = []
nome_modulo = ""

root = tk.Tk()
root.title("Gerador Automático de Testes")
root.geometry("1000x650")

top_frame = tk.Frame(root)
top_frame.pack(pady=5)

middle_frame = tk.Frame(root)
middle_frame.pack(fill="both", expand=True, padx=10)

bottom_frame = tk.Frame(root)
bottom_frame.pack(fill="both", expand=True, padx=10, pady=10)

def abrir_ficheiro():
    global caminho_codigo, funcoes_encontradas, nome_modulo
    caminho_codigo = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if not caminho_codigo:
        return

    with open(caminho_codigo, 'r') as f:
        codigo = f.read()

    nome_modulo = nome_sem_extensao(caminho_codigo)
    analisador = CodeAnalyzer(codigo)
    funcoes_encontradas = analisador.extract_functions()

    gerar_testes(funcoes_encontradas, nome_modulo=nome_modulo)

    codigo_box.delete('1.0', tk.END)
    codigo_box.insert(tk.END, codigo)

    lista_funcoes.delete(0, tk.END)
    for func in funcoes_encontradas:
        lista_funcoes.insert(tk.END, func.name)

    atualizar_testes_gerados()

    messagebox.showinfo("Sucesso", "Testes gerados com sucesso!")

def carregar_pasta_projeto():
    global nome_modulo
    pasta = filedialog.askdirectory()
    if not pasta:
        return

    total_testes = 0
    lista_funcoes.delete(0, tk.END)
    codigo_box.delete('1.0', tk.END)
    testes_box.delete('1.0', tk.END)

    for raiz, dirs, ficheiros in os.walk(pasta):
        for ficheiro in ficheiros:
            if ficheiro.endswith(".py"):
                caminho_completo = os.path.join(raiz, ficheiro)
                nome_modulo = nome_sem_extensao(ficheiro)

                with open(caminho_completo, 'r') as f:
                    codigo = f.read()

                try:
                    analisador = CodeAnalyzer(codigo)
                    funcoes = analisador.extract_functions()

                    if not funcoes:
                        continue

                    gerar_testes(funcoes, nome_modulo=nome_modulo, caminho_modulo=caminho_completo)

                    codigo_box.insert(tk.END, f"# {ficheiro}\n{codigo}\n\n")
                    for func in funcoes:
                        lista_funcoes.insert(tk.END, f"{ficheiro}: {func.name}")
                    atualizar_testes_gerados()
                    total_testes += len(funcoes)
                except Exception as e:
                    print(f"Erro ao processar {ficheiro}: {e}")

    messagebox.showinfo("Concluído", f"Testes gerados para {total_testes} funções em múltiplos módulos.")

def atualizar_testes_gerados():
    caminho_teste = os.path.join("tests", f"test_{nome_modulo}.py")
    if os.path.exists(caminho_teste):
        with open(caminho_teste, 'r') as f:
            conteudo = f.read()
        testes_box.delete('1.0', tk.END)
        testes_box.insert(tk.END, conteudo)

def guardar_testes_editados():
    caminho_teste = os.path.join("tests", f"test_{nome_modulo}.py")
    with open(caminho_teste, 'w') as f:
        novo_conteudo = testes_box.get("1.0", tk.END)
        f.write(novo_conteudo)
    messagebox.showinfo("Guardado", "Alterações aos testes guardadas com sucesso.")

def regenerar_testes():
    if not caminho_codigo:
        return
    with open(caminho_codigo, 'r') as f:
        codigo = f.read()
    analisador = CodeAnalyzer(codigo)
    funcoes = analisador.extract_functions()
    gerar_testes(funcoes, nome_modulo=nome_modulo, caminho_modulo=caminho_completo)
    atualizar_testes_gerados()
    messagebox.showinfo("Atualizado", "Testes regenerados com sucesso!")

def correr_testes():
    guardar_testes_editados()
    output_box.delete('1.0', tk.END)
    resultado = executar_testes(retornar=True)
    output_box.insert(tk.END, resultado)

# BOTÕES
btn_carregar = tk.Button(top_frame, text="Carregar Código Python", command=abrir_ficheiro)
btn_carregar.pack(side="left", padx=10)

btn_carregar_pasta = tk.Button(top_frame, text="Carregar Projeto (pasta)", command=carregar_pasta_projeto)
btn_carregar_pasta.pack(side="left", padx=10)

btn_guardar_testes = tk.Button(top_frame, text="Guardar Testes Editados", command=guardar_testes_editados)
btn_guardar_testes.pack(side="left", padx=10)

btn_regenerar = tk.Button(top_frame, text="Regenerar Testes", command=regenerar_testes)
btn_regenerar.pack(side="left", padx=10)

btn_correr = tk.Button(top_frame, text="Executar Testes", command=correr_testes)
btn_correr.pack(side="left", padx=10)


# ÁREAS VISUAIS
codigo_box = scrolledtext.ScrolledText(middle_frame, height=15, width=60)
codigo_box.pack(side="left", padx=5)

lista_funcoes = tk.Listbox(middle_frame, height=15, width=25)
lista_funcoes.pack(side="left", padx=5)

testes_box = scrolledtext.ScrolledText(middle_frame, height=15, width=60)
testes_box.pack(side="left", padx=5)

output_box = scrolledtext.ScrolledText(bottom_frame, height=10)
output_box.pack(fill="both", expand=True)

root.mainloop()