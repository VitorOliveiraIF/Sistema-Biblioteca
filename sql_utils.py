import mariadb

def consultar_localidade_por_idlivro(id_livro):
    try:
        # Conectar ao banco de dados
        conexao = mariadb.connect(
            user="",
            password="",
            host="",
            port=,
            database=""
        )

        # Cursor
        sql = conexao.cursor()

        # Consulta SQL
        consulta = """
            SELECT loc.Nome AS NomeLocalidade
            FROM livros l
            INNER JOIN localidade loc ON l.IDLocalidade = loc.ID
            WHERE l.ID = ?
        """

        # Executar a consulta com o parâmetro
        sql.execute(consulta, (id_livro,))

        # Obter os resultados
        resultado = sql.fetchone()

        # Fechar o cursor e a conexão
        sql.close()
        conexao.close()

        # Retornar o nome da localidade
        return resultado[0] if resultado else None

    except mariadb.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def consultar_IDlocalidade_por_idlivro(id_livro):
    try:
        # Conectar ao banco de dados
        conexao = mariadb.connect(
            user="",
            password="",
            host="",
            port=,
            database=""
        )

        # Cursor
        sql = conexao.cursor()

        # Consulta SQL
        consulta = """
            SELECT IDLocalidade
            FROM livros
            WHERE ID = ?
        """

        # Executar a consulta com o parâmetro
        sql.execute(consulta, (id_livro,))

        # Obter os resultados
        resultado = sql.fetchone()

        # Fechar o cursor e a conexão
        sql.close()
        conexao.close()

        # Retornar o nome da localidade
        return resultado[0] if resultado else None

    except mariadb.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def nome_do_cliente_por_id(id_cliente):
    try:
        # Conectar ao banco de dados
        conexao = mariadb.connect(
        user="",
        password="",
        host="",
        port=,
        database=""
    )

        # Criar um cursor para executar a consulta
        cursor = conexao.cursor()

        # Consulta SQL
        consulta = """
            SELECT nome
            FROM clientes
            WHERE ID = ?
        """

        # Executar a consulta com o ID do cliente como parâmetro
        cursor.execute(consulta, (id_cliente,))

        # Obter o resultado da consulta
        resultado = cursor.fetchone()

        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

        # Retornar o nome do cliente
        return resultado[0] if resultado else None

    except mariadb.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def estado_do_livro_por_id(id_livro):
    try:
        # Conectar ao banco de dados
        conexao = mariadb.connect(
        user="",
        password="",
        host="",
        port=3306,
        database=""
    )

        # Criar um cursor para executar a consulta
        cursor = conexao.cursor()

        # Consulta SQL
        consulta = """
            SELECT emprestado
            FROM livros
            WHERE ID = ?
        """

        # Executar a consulta com o ID do livro como parâmetro
        cursor.execute(consulta, (id_livro,))

        # Obter o resultado da consulta
        resultado = cursor.fetchone()

        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

        # Retornar o estado do livro
        return resultado[0] if resultado else None

    except mariadb.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def livros_em_posse_por_id(id_cliente):
    try:
        # Conectar ao banco de dados
        conexao = mariadb.connect(
            user="",
            password="",
            host="",
            port=,
            database=""
        )

        # Criar um cursor para executar a consulta
        cursor = conexao.cursor()

        # Consulta SQL
        consulta = """
            SELECT NumEmp
            FROM clientes
            WHERE ID = ?;
        """

        # Executar a consulta com o ID do cliente como parâmetro
        cursor.execute(consulta, (id_cliente,))

        # Obter o resultado da consulta
        resultado = cursor.fetchone()

        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

        # Verificar se houve algum resultado
        if resultado:
            # Retornar o valor do campo NumEmp como um número inteiro
            return int(resultado[0])
        else:
            # Se não houver resultado, retornar None ou um valor padrão, dependendo do caso
            return None  # ou return 0 ou outro valor padrão, se necessário
    
    except mariadb.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None  # ou outro tratamento de erro, se desejado

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

def mudar_estado_livro(id_livro):
    try:
        # Conectar ao banco de dados
        conexao = mariadb.connect(
            user="",
            password="",
            host="",
            port=,
            database=""
        )

        # Criar um cursor para executar a consulta
        cursor = conexao.cursor()

        consulta_estado = """
            SELECT emprestado
            FROM livros
            WHERE ID = ?
        """

        # Executar a consulta para obter o estado atual do livro
        cursor.execute(consulta_estado, (id_livro,))
        estado_atual = cursor.fetchone()[0]

        # Inverter o estado do livro
        novo_estado = 1 if estado_atual == 0 else 0

        consulta_atualizacao = """
            UPDATE livros
            SET emprestado = ?
            WHERE ID = ?
        """

        # Executar a consulta para atualizar o estado do livro
        cursor.execute(consulta_atualizacao, (novo_estado, id_livro))

        # Commit para aplicar as mudanças no banco de dados
        conexao.commit()

        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

        print("Alteração realizada com sucesso")

        return novo_estado

    except mariadb.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None  # ou outro tratamento de erro, se desejado

#///////////////////////////////////////////////////////////////////////////////////////////////

def sortear_id_func(IDloc_livro):
    try:
        # Conectar ao banco de dados
        conexao = mariadb.connect(
            user="",
            password="",
            host="",
            port=,
            database=""
        )

        cursor = conexao.cursor()

        # Consulta SQL para selecionar um funcionário aleatório da mesma localização do livro
        consulta_funcionarios = """
            SELECT ID
            FROM funcionarios
            WHERE IDLocalidade = ?  -- Filtrar por localização
            ORDER BY RAND()  -- Ordenar aleatoriamente os funcionários
            LIMIT 1  -- Limitar o resultado a 1 funcionário
        """

        # Executar a consulta com o ID da localização do livro como parâmetro
        cursor.execute(consulta_funcionarios, (IDloc_livro,))

        # Obter o ID do funcionário sorteado
        id_funcionario = cursor.fetchone()[0]

        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

        return id_funcionario
    
    except mariadb.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None  # ou outro tratamento de erro, se desejado

#///////////////////////////////////////////////////////////////////////////////////////////////    

def aumenta_emprest_func(id_func):
    try:
        # Conectar ao banco de dados
        conexao = mariadb.connect(
            user="",
            password="",
            host="",
            port=,
            database=""
        )

        cursor = conexao.cursor()

        consulta_emprestimos = """
            SELECT LivrosEmp
            FROM funcionarios
            WHERE ID = ?
        """

        # Executar a consulta com o ID do funcionário como parâmetro
        cursor.execute(consulta_emprestimos, (id_func,))

        # Obter o resultado da consulta
        resultado = cursor.fetchone()

        if resultado:
            # Extrair o número atual de empréstimos
            emprestimos_atuais = resultado[0]

            # Incrementar o número de empréstimos em 1
            novo_numero_emprestimos = emprestimos_atuais + 1

            # Consulta SQL para atualizar o número de empréstimos do funcionário
            atualizar_emprestimos = """
                UPDATE funcionarios
                SET LivrosEmp = ?
                WHERE ID = ?
            """

            # Executar a consulta para atualizar o número de empréstimos do funcionário
            cursor.execute(atualizar_emprestimos, (novo_numero_emprestimos, id_func))

            # Commit para aplicar as mudanças no banco de dados
            conexao.commit()

            print("Número de empréstimos do funcionário aumentado com sucesso!")
        else:
            print("Funcionário não encontrado.")

        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

    except mariadb.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

#///////////////////////////////////////////////////////////////////////////////////////////////   

def nome_func_porID(id_func):

    try:
        # Conectar ao banco de dados
        conexao = mariadb.connect(
            user="",
            password="",
            host="",
            port=,
            database=""
        )

        cursor = conexao.cursor()

        # Consulta SQL para obter o nome do funcionário pelo ID
        consulta_nome_funcionario = """
            SELECT nome
            FROM funcionarios
            WHERE ID = ?
        """

        # Executar a consulta com o ID do funcionário como parâmetro
        cursor.execute(consulta_nome_funcionario, (id_func,))

        # Obter o resultado da consulta
        resultado = cursor.fetchone()

        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

        # Retornar o nome do funcionário
        return resultado[0] if resultado else None

    except mariadb.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    
#///////////////////////////////////////////////////////////////////////////////////////////////   

def aumentar_livros_emprestados_cliente(id_cliente):
    try:
        # Conectar ao banco de dados
        conexao = mariadb.connect(
            user="",
            password="",
            host="",
            port=,
            database=""
        )

        # Criar um cursor para executar a consulta
        cursor = conexao.cursor()

        # Consulta SQL para aumentar o número de livros emprestados pelo cliente
        consulta = """
            UPDATE clientes
            SET NumEmp = NumEmp + 1
            WHERE id = ?
        """

        # Executar a consulta com o ID do cliente como parâmetro
        cursor.execute(consulta, (id_cliente,))

        # Commit para aplicar as mudanças no banco de dados
        conexao.commit()

        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

        print("Número de livros emprestados pelo cliente", id_cliente, "aumentado com sucesso.")

    except mariadb.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

#///////////////////////////////////////////////////////////////////////////////////////////////   

def registro_emp(idLivro, idCliente, id_func, IDloc_livro, operacao):
    try:
        # Conectar ao banco de dados
        conexao = mariadb.connect(
            user="",
            password="",
            host="",
            port=,
            database=""
        )

        # Criar um cursor para executar a consulta
        cursor = conexao.cursor()

        # Consulta SQL para inserir um registro na tabela de empréstimos
        consulta = """
            INSERT INTO emprestimos (idLivro, idCliente, idfuncionario, idlocalidade, operacao)
            VALUES (?, ?, ?, ?, ?)
        """

        # Executar a consulta com os parâmetros fornecidos
        cursor.execute(consulta, (idLivro, idCliente, id_func, IDloc_livro, operacao))

        # Commit para aplicar as mudanças no banco de dados
        conexao.commit()

        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

        print("Registro de empréstimo gerado com sucesso.")

    except mariadb.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

#///////////////////////////////////////////////////////////////////////////////////////////////

def registro_dev(idLivro, idCliente, id_func, IDloc_livro, operacao):
    try:
        # Conectar ao banco de dados
        conexao = mariadb.connect(
            user="",
            password="",
            host="",
            port=,
            database=""
        )

        # Criar um cursor para executar a consulta
        cursor = conexao.cursor()

        # Consulta SQL para inserir um registro na tabela de empréstimos
        consulta = """
            INSERT INTO emprestimos (idLivro, idCliente, idfuncionario, idlocalidade, operacao)
            VALUES (?, ?, ?, ?, ?)
        """

        # Executar a consulta com os parâmetros fornecidos
        cursor.execute(consulta, (idLivro, idCliente, id_func, IDloc_livro, operacao))

        # Commit para aplicar as mudanças no banco de dados
        conexao.commit()

        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

        print("Registro de devolução gerado com sucesso.")

    except mariadb.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

#///////////////////////////////////////////////////////////////////////////////////////////////

def id_cliente_por_cpf(cpf):

    try:
        # Conectar ao banco de dados
        conexao = mariadb.connect(
            user="",
            password="",
            host="",
            port=,
            database=""
        )

        # Criar um cursor para executar a consulta
        cursor = conexao.cursor()

        # Consulta SQL para obter o ID do cliente pelo CPF
        consulta = """
            SELECT ID
            FROM clientes
            WHERE CPF = ?
        """

        # Executar a consulta com o CPF do cliente como parâmetro
        cursor.execute(consulta, (cpf,))

        # Obter o resultado da consulta
        resultado = cursor.fetchone()

        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

        # Retornar o ID do cliente
        return resultado[0] if resultado else None

    except mariadb.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    
#///////////////////////////////////////////////////////////////////////////////////////////////

def nome_livro_por_ID(id_livro):

    try:
        # Conectar ao banco de dados
        conexao = mariadb.connect(
            user="",
            password="",
            host="",
            port=,
            database=""
        )

        # Criar um cursor para executar a consulta
        cursor = conexao.cursor()

        # Consulta SQL para obter o ID do cliente pelo CPF
        consulta = """
            SELECT nome
            FROM livros
            WHERE id = ?
        """

        # Executar a consulta com o CPF do cliente como parâmetro
        cursor.execute(consulta, (id_livro,))

        # Obter o resultado da consulta
        resultado = cursor.fetchone()

        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

        # Retornar o ID do cliente
        return resultado[0] if resultado else None

    except mariadb.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

#///////////////////////////////////////////////////////////////////////////////////////////////  

def diminui_livros_emprestados_cliente(id_cliente):
    try:
        # Conectar ao banco de dados
        conexao = mariadb.connect(
            user="",
            password="",
            host="",
            port=,
            database=""
        )

        # Criar um cursor para executar a consulta
        cursor = conexao.cursor()

        # Consulta SQL para aumentar o número de livros emprestados pelo cliente
        consulta = """
            UPDATE clientes
            SET NumEmp = NumEmp - 1
            WHERE id = ?
        """

        # Executar a consulta com o ID do cliente como parâmetro
        cursor.execute(consulta, (id_cliente,))

        # Commit para aplicar as mudanças no banco de dados
        conexao.commit()

        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

        print("Número de livros emprestados pelo cliente", id_cliente, "aumentado com sucesso.")

    except mariadb.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")