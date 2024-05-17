import tkinter as tk
from tkinter import messagebox
from sql_utils import consultar_localidade_por_idlivro, estado_do_livro_por_id, livros_em_posse_por_id
from sql_utils import nome_do_cliente_por_id, mudar_estado_livro, sortear_id_func, consultar_IDlocalidade_por_idlivro
from sql_utils import aumenta_emprest_func, nome_func_porID, aumentar_livros_emprestados_cliente, registro_emp
from sql_utils import id_cliente_por_cpf, nome_livro_por_ID, registro_dev, diminui_livros_emprestados_cliente

def verificar_cpf():
    # Função para verificar o CPF digitado pelo usuário

    # Obtendo o CPF digitado pelo usuário
    cpf_cliente = entry_cpf.get()

    # Continuar solicitando o CPF até que um ID de cliente válido seja retornado
    while True:
        id_cliente = id_cliente_por_cpf(int(cpf_cliente))
        if id_cliente is not None:
            nome_cliente = nome_do_cliente_por_id(id_cliente)
            abrir_janela_escolha(id_cliente, nome_cliente)
            break
        else:
            messagebox.showerror("CPF inválido", "CPF inválido. Por favor, digite novamente.")
            return

def abrir_janela_escolha(id_cliente, nome_cliente):
    # Função para abrir uma nova janela para escolher entre devolver ou pegar emprestado

    # Criar uma nova janela para a escolha
    nova_janela = tk.Toplevel()
    nova_janela.title("Escolha")
    nova_janela.geometry("300x150")

    # Botão para realizar empréstimo
    btn_emprestimo = tk.Button(nova_janela, text="Pegar livro", command=lambda: abrir_janela_idlivro(id_cliente, nome_cliente, nova_janela))
    btn_emprestimo.pack(pady=10)

    # Botão para realizar devolução
    btn_devolucao = tk.Button(nova_janela, text="Devolver", command=lambda: realizar_devolucao(id_cliente, nome_cliente, nova_janela))
    btn_devolucao.pack(pady=10)

def abrir_janela_idlivro(id_cliente, nome_cliente, janela):
    # Função para abrir uma nova janela para inserir o ID do livro

    # Criar uma nova janela para inserir o ID do livro
    nova_janela = tk.Toplevel()
    nova_janela.title("Informe o ID do livro")
    nova_janela.geometry("300x150")

    # Label e Entry para o ID do livro
    label_id_livro = tk.Label(nova_janela, text="Informe o ID do livro:")
    label_id_livro.pack()
    entry_id_livro = tk.Entry(nova_janela)
    entry_id_livro.pack(pady=5)

    # Botão para realizar o empréstimo
    btn_emprestimo = tk.Button(nova_janela, text="Realizar Empréstimo", command=lambda: realizar_emprestimo(entry_id_livro.get(), id_cliente, nome_cliente, nova_janela))
    btn_emprestimo.pack(pady=10)

    # Fechar a janela anterior
    janela.destroy()

def realizar_emprestimo(id_livro, id_cliente, nome_cliente, janela):
    loc_livro = consultar_localidade_por_idlivro(int(id_livro))
    messagebox.showinfo("Localidade do livro", f"O livro está em {loc_livro}")

    estado_livro = estado_do_livro_por_id(int(id_livro))
    if estado_livro == 1:
        messagebox.showerror("Livro indisponível", "O livro está indisponível para empréstimo")
        return

    # Obtendo o ID da localidade do livro
    id_loc_livro = consultar_IDlocalidade_por_idlivro(int(id_livro))

    # Confirmando o empréstimo
    confirmar = messagebox.askyesno("Confirmação", "Deseja confirmar o empréstimo desse livro?")
    if confirmar:
        id_func = sortear_id_func(id_loc_livro)
        nome_funcionario = nome_func_porID(id_func)
        nome_livro = nome_livro_por_ID(int(id_livro))

        # Realizando as operações de banco de dados
        mudar_estado_livro(int(id_livro))
        aumenta_emprest_func(id_func)
        aumentar_livros_emprestados_cliente(id_cliente)
        registro_emp(int(id_livro), id_cliente, id_func, id_loc_livro, 1)

        messagebox.showinfo("Empréstimo realizado", f"Operação bem-sucedida. O livro {nome_livro} foi emprestado para {nome_cliente} pelo funcionário {nome_funcionario} na cidade de {loc_livro}")

    else:
        messagebox.showinfo("Operação cancelada", "Operação de empréstimo cancelada")

    # Fechar a janela atual
    janela.destroy()

    janela.destroy()

def realizar_devolucao(id_cliente, nome_cliente, janela):
    # Função para realizar a operação de devolução

    # Obtendo o número de livros em posse pelo cliente
    livros_posse = livros_em_posse_por_id(id_cliente)

    # Verificando se o cliente não possui nenhum livro em posse
    if livros_posse == 0:
        messagebox.showerror("Nenhum livro em posse", f"Você não possui nenhum livro em posse para devolução.")
        janela.destroy()
        return

    # Criar uma nova janela para inserir o ID do livro a ser devolvido
    nova_janela = tk.Toplevel()
    nova_janela.title("Informe o ID do livro a ser devolvido")
    nova_janela.geometry("300x150")

    # Label e Entry para o ID do livro
    label_id_livro = tk.Label(nova_janela, text="Informe o ID do livro a ser devolvido:")
    label_id_livro.pack()
    entry_id_livro = tk.Entry(nova_janela)
    entry_id_livro.pack(pady=5)

    # Botão para confirmar a devolução
    btn_devolucao = tk.Button(nova_janela, text="Confirmar Devolução", command=lambda: confirmar_devolucao(entry_id_livro.get(), id_cliente, nome_cliente, nova_janela))
    btn_devolucao.pack(pady=10)

    # Fechar a janela anterior
    janela.destroy()



#/////////////////////////////////////////////////////////////////////////////////////////////////////////
def confirmar_devolucao(id_livro, id_cliente, nome_cliente, janela):

    # ID da localidade do livro
    IDlocLivro = consultar_IDlocalidade_por_idlivro(id_livro)

    # Confirmar a devolução
    confirmar = messagebox.askyesno("Confirmação", "Deseja confirmar a devolução desse livro?")
    if confirmar:
        # ID do funcionário responsável pela devolução
        id_func = sortear_id_func(IDlocLivro)
        nome_funcionario = nome_func_porID(id_func)

        # Nome do livro
        nome_livro = nome_livro_por_ID(int(id_livro))

        # Alterar o estado do livro para disponível
        mudar_estado_livro(int(id_livro))

        # Reduzir o número de livros em posse do cliente
        diminui_livros_emprestados_cliente(id_cliente)

        # Registrar a devolução no banco de dados
        registro_dev(int(id_livro), id_cliente, id_func, IDlocLivro, 2)

        messagebox.showinfo("Devolução realizada", f"Operação bem-sucedida. O livro {nome_livro} foi devolvido por {nome_cliente} ao funcionário {nome_funcionario}.")
    else:
        messagebox.showinfo("Operação cancelada", "Operação de devolução cancelada.")

    # Fechar a janela atual
    janela.destroy()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Criando a janela principal
root = tk.Tk()
root.title("Sistema de Empréstimo de Livros")
root.geometry("300x150")

# Entrada para o CPF do cliente
label_cpf = tk.Label(root, text="Digite o seu CPF:")
label_cpf.pack()
entry_cpf = tk.Entry(root)
entry_cpf.pack(pady=5)

# Botão para verificar o CPF
btn_verificar_cpf = tk.Button(root, text="Verificar CPF", command=verificar_cpf)
btn_verificar_cpf.pack(pady=10)

# Iniciando o loop principal
root.mainloop()
