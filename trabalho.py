import mysql.connector

# Função para conectar ao banco de dados
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",       
        password="123456",     
        database="estoque_mercado"
    )

# CRUD para a tabela Produto
def create_produto(nome, preco, descricao):
    conn = connect_db()
    cursor = conn.cursor()

    try:
        # Inserir o produto
        sql_produto = "INSERT INTO Produto (nome, preco, descricao) VALUES (%s, %s, %s)"
        cursor.execute(sql_produto, (nome, preco, descricao))

        # Obter o ID do produto recém-inserido
        produto_id = cursor.lastrowid

        # Inserir no estoque com saldo inicial 0
        sql_estoque = "INSERT INTO Estoque (fk_produto, saldo) VALUES (%s, %s)"
        cursor.execute(sql_estoque, (produto_id, 0))

        conn.commit()
        print(f"Produto '{nome}' cadastrado com sucesso e adicionado ao estoque com saldo inicial 0.")
    except mysql.connector.Error as err:
        print(f"Erro ao cadastrar produto: {err}")
    finally:
        conn.close()

def read_produtos():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produto")
    produtos = cursor.fetchall()
    print("\n--- Lista de Produtos ---")
    for produto in produtos:
        print(f"ID: {produto[0]}, Nome: {produto[1]}, Preço: {produto[2]}, Descrição: {produto[3]}")
    conn.close()

def update_produto(id_produto, nome, preco, descricao):
    conn = connect_db()
    cursor = conn.cursor()
    sql = """
    UPDATE Produto
    SET nome = %s, preco = %s, descricao = %s
    WHERE id_produto = %s
    """
    cursor.execute(sql, (nome, preco, descricao, id_produto))
    conn.commit()
    print(f"Produto com ID {id_produto} atualizado com sucesso!")
    conn.close()

def delete_produto(id_produto):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "DELETE FROM Produto WHERE id_produto = %s"
    cursor.execute(sql, (id_produto,))
    conn.commit()
    print(f"Produto com ID {id_produto} removido com sucesso!")
    conn.close()

# CRUD para a tabela Fornecedor
def create_fornecedor(nome, contato):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "INSERT INTO Fornecedor (nome, contato) VALUES (%s, %s)"
    cursor.execute(sql, (nome, contato))
    conn.commit()
    print(f"Fornecedor '{nome}' inserido com sucesso!")
    conn.close()

def read_fornecedores():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Fornecedor")
    fornecedores = cursor.fetchall()
    print("\n--- Lista de Fornecedores ---")
    for fornecedor in fornecedores:
        print(f"ID: {fornecedor[0]}, Nome: {fornecedor[1]}, Contato: {fornecedor[2]}")
    conn.close()

def update_fornecedor(id_fornecedor, nome, contato):
    conn = connect_db()
    cursor = conn.cursor()
    sql = """
    UPDATE Fornecedor
    SET nome = %s, contato = %s
    WHERE id_fornecedor = %s
    """
    cursor.execute(sql, (nome, contato, id_fornecedor))
    conn.commit()
    print(f"Fornecedor com ID {id_fornecedor} atualizado com sucesso!")
    conn.close()

def delete_fornecedor(id_fornecedor):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "DELETE FROM Fornecedor WHERE id_fornecedor = %s"
    cursor.execute(sql, (id_fornecedor,))
    conn.commit()
    print(f"Fornecedor com ID {id_fornecedor} removido com sucesso!")
    conn.close()

# Atualização de Estoque
def update_estoque_entrada(fk_produto, quantidade):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "UPDATE Estoque SET saldo = saldo + %s WHERE fk_produto = %s"
    cursor.execute(sql, (quantidade, fk_produto))
    conn.commit()
    print(f"Estoque do produto {fk_produto} atualizado após entrada!")
    conn.close()

def update_estoque_saida(fk_produto, quantidade):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "UPDATE Estoque SET saldo = saldo - %s WHERE fk_produto = %s"
    cursor.execute(sql, (quantidade, fk_produto))
    conn.commit()
    print(f"Estoque do produto {fk_produto} atualizado após saída!")
    conn.close()

def read_estoque():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT Produto.nome, Estoque.saldo
    FROM Estoque
    INNER JOIN Produto ON Estoque.fk_produto = Produto.id_produto
    """)
    estoque = cursor.fetchall()
    print("\n--- Estoque Atual ---")
    for item in estoque:
        print(f"Produto: {item[0]}, Saldo: {item[1]}")
    conn.close()

# Menu principal
def menu():
    while True:
        print("\n--- Sistema de Estoque ---")
        print("1. Cadastrar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Excluir Produto")
        print("5. Cadastrar Fornecedor")
        print("6. Listar Fornecedores")
        print("7. Atualizar Fornecedor")
        print("8. Excluir Fornecedor")
        print("9. Atualizar Estoque (Entrada)")
        print("10. Atualizar Estoque (Saída)")
        print("11. Ver Estoque")
        print("0. Sair")
        
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            descricao = input("Descrição do produto: ")
            create_produto(nome, preco, descricao)
        elif opcao == 2:
            read_produtos()
        elif opcao == 3:
            id_produto = int(input("ID do produto: "))
            nome = input("Novo nome: ")
            preco = float(input("Novo preço: "))
            descricao = input("Nova descrição: ")
            update_produto(id_produto, nome, preco, descricao)
        elif opcao == 4:
            id_produto = int(input("ID do produto: "))
            delete_produto(id_produto)
        elif opcao == 5:
            nome = input("Nome do fornecedor: ")
            contato = input("Contato do fornecedor: ")
            create_fornecedor(nome, contato)
        elif opcao == 6:
            read_fornecedores()
        elif opcao == 7:
            id_fornecedor = int(input("ID do fornecedor: "))
            nome = input("Novo nome: ")
            contato = input("Novo contato: ")
            update_fornecedor(id_fornecedor, nome, contato)
        elif opcao == 8:
            id_fornecedor = int(input("ID do fornecedor: "))
            delete_fornecedor(id_fornecedor)
        elif opcao == 9:
            fk_produto = int(input("ID do produto: "))
            quantidade = int(input("Quantidade a adicionar: "))
            update_estoque_entrada(fk_produto, quantidade)
        elif opcao == 10:
            fk_produto = int(input("ID do produto: "))
            quantidade = int(input("Quantidade a retirar: "))
            update_estoque_saida(fk_produto, quantidade)
        elif opcao == 11:
            read_estoque()
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# Executa o menu
menu()
