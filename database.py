import mysql.connector
import datetime

class DataBase:
    def __init__(self, host='localhost', user='root', password='8456', database='sistema'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexão ao MySQL estabelecida com sucesso.")
        except mysql.connector.Error as e:
            print("Erro ao conectar ao MySQL:", e)

    
    def close_connection(self):
        if self.connection is not None:
            try:
                self.connection.close()
                print("Conexão ao MySQL fechada com sucesso.")
            except mysql.connector.Error as e:
                print("Erro ao fechar a conexão:", e)
        else:
            print("Não há conexão para fechar.")

    def create_database(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            print("Banco de dados criado com sucesso.")
        except mysql.connector.Error as e:
            print("Erro ao criar o banco de dados:", e)
        finally:
            self.close_connection()

            
    def create_table_users(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"USE {self.database}")
            cursor.execute(""" 
                CREATE TABLE IF NOT EXISTS usuario(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    user VARCHAR(255) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    access VARCHAR(255) NOT NULL
                )
            """)
            print("Tabela 'usuario' criada com sucesso.")
        except mysql.connector.Error as e:
            print("Erro ao criar a tabela 'usuario':", e)
        finally:
            self.close_connection()    
     
    def create_table_clientes(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"USE {self.database}")
            cursor.execute(""" 
                CREATE TABLE IF NOT EXISTS clientes(
                    codigo INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    rg VARCHAR(255) UNIQUE NOT NULL,
                    cpf VARCHAR(255) NOT NULL,
                    telefone VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    endereco VARCHAR(255) NOT NULL,
                    datacadastro DATETIME NOT NULL
                )
            """)
            print("Tabela 'clientes' criada com sucesso.")
        except mysql.connector.Error as e:
            print("Erro ao criar a tabela 'clientes':", e)
        finally:
            self.close_connection()
            
    def create_table_produtos(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"USE {self.database}")
            cursor.execute(""" 
                CREATE TABLE IF NOT EXISTS produtos(
                        codigo INT AUTO_INCREMENT PRIMARY KEY,
                        nome VARCHAR(255) NOT NULL,
                        categoria VARCHAR(255) NOT NULL,
                        fabricante VARCHAR(255) NOT NULL,
                        quantidade INT NOT NULL,
                        garantia VARCHAR(255),      
                        valor DECIMAL(10, 2) NOT NULL,
                        codigoDeBarra VARCHAR(255) UNIQUE NOT NULL
                    )
                """)
            print("Tabela 'produtos' criada com sucesso.")
        except mysql.connector.Error as e:
            print("Erro ao criar a tabela 'produtos':", e)
        finally:
            self.close_connection()   
                
    def create_table_vendas(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"USE {self.database}")
            cursor.execute(""" 
                CREATE TABLE IF NOT EXISTS vendas(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    cliente VARCHAR(255) NOT NULL,
                    produto VARCHAR(255) NOT NULL,
                    valor DECIMAL(64, 2) NOT NULL,
                    forma_pagamento VARCHAR(255) NOT NULL,
                    status_pagamento VARCHAR(255) NOT NULL,
                    data_venda DATETIME NOT NULL
                )
            """)
            print("Tabela 'vendas' criada com sucesso.")
        except mysql.connector.Error as e:
            print("Erro ao criar a tabela 'vendas':", e)
        finally:
            self.close_connection()     
            
    def create_table_financeiro(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"USE {self.database}")
            cursor.execute(""" 
                CREATE TABLE IF NOT EXISTS financeiro(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    cliente VARCHAR(255) NOT NULL,
                    produto VARCHAR(255) NOT NULL,
                    valor DECIMAL(64, 2) NOT NULL,
                    valorTotal DECIMAL(64, 2) NOT NULL,
                    forma_pagamento VARCHAR(255) NOT NULL,
                    status_pagamento VARCHAR(255) NOT NULL,
                    data_venda DATETIME NOT NULL
                )
            """)
            print("Tabela 'financeiro' criada com sucesso.")
        except mysql.connector.Error as e:
            print("Erro ao criar a tabela 'vendas':", e)
        finally:
            self.close_connection()                   
            
class Clientes:
    def __init__(self, nome, rg, cpf, telefone, email, endereco, datacadastro=None):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.datacadastro = datacadastro or datetime.datetime.now()  # Usando a data atual se não for especificada

class ClientesBanco:
    def __init__(self, database):
        self.database = database
        
    def salvar_edicao(self, ui_editarCliente):
        # Seu código para salvar a edição aqui
        self.main_window.load_cliente_table()  # Chamando o método load_cliente_table da MainWindow
        
    def insert_cliente(self, cliente):
        try:
            self.database.connect()
            cursor = self.database.connection.cursor()
            cursor.execute(""" 
                INSERT INTO clientes(nome, rg, cpf, telefone, email, endereco, datacadastro) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (
                    cliente.nome, cliente.rg, cliente.cpf, cliente.telefone, 
                    cliente.email, cliente.endereco, cliente.datacadastro
                ))
            self.database.connection.commit()
            print("Cliente inserido com sucesso.")
        except mysql.connector.Error as e:
            print("Erro ao inserir Cliente:", e)
        finally:
            self.database.close_connection()    
                            
class Produtos:
    def __init__(self, nome, categoria, fabricante, quantidade, garantia, valor, codigoDeBarra):
        self.nome = nome
        self.categoria = categoria
        self.fabricante = fabricante
        self.quantidade = quantidade
        self.garantia = garantia
        self.valor = valor
        self.codigoDeBarra = codigoDeBarra

class ProdutosBanco:
    def __init__(self, main_window,database):
        self.main_window = main_window
        self.database = database
    
    def salvar_edicao(self, ui_editarProdutos):
        # Seu código para salvar a edição aqui
        self.main_window.load_produto_table()  # Chamando o método load_produto_table da MainWindow
        
    # def load_table(self):
    #     self.load_table_produtos()
        
    def insert_produtos(self, produtos):
        try:
            self.database.connect()
            cursor = self.database.connection.cursor()
            cursor.execute(""" 
                INSERT INTO produtos(nome, categoria, fabricante, quantidade,  garantia,valor, codigoDeBarra) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (
                    produtos.nome, produtos.categoria, produtos.fabricante, produtos.quantidade, 
                    produtos.garantia, produtos.valor, produtos.codigoDeBarra
                ))
            self.database.connection.commit()
            print("Produto inserido com sucesso.")
        except mysql.connector.Error as e:
            print("Erro ao inserir Produto:", e)
        finally:
            self.database.close_connection()    
                          
class User:
    def __init__(self, name, user, password, access):
        self.name = name
        self.user = user
        self.password = password
        self.access = access    
        
class UserManager:
    def __init__(self, database):
        self.database = database
        
    def insert_user(self, user):
        try:
            self.database.connect()
            cursor = self.database.connection.cursor()
            cursor.execute(""" 
                INSERT INTO usuario(name, user, password, access) VALUES (%s, %s, %s, %s)
                """, (user.name, user.user, user.password, user.access))
            self.database.connection.commit()
            print("Usuário inserido com sucesso.")
        except mysql.connector.Error as e:
            print("Erro ao inserir usuário:", e)
        finally:
            self.database.close_connection()       
        
    def check_user(self, user, password):
        try:
            self.database.connect()
            cursor = self.database.connection.cursor()
            cursor.execute("SELECT * FROM usuario WHERE user = %s", (user,))
        
            row = cursor.fetchone()
            if row:
                stored_password = row[3]  # Índice 3 representa a coluna de senhas na tabela
                if password == stored_password:
                    access = row[4]  # Índice 4 representa a coluna de acesso na tabela
                    return access
                else:
                    print("Senha incorreta.")
                    return None
            else:
                print("Usuário não encontrado.")
                return None
        except mysql.connector.Error as e:
            print("Erro ao verificar usuário:", e)
            return None
        finally:
            self.database.close_connection()

class Vendas: 
    def __init__(self, cliente, produto,valor, forma_pagamento, status_pagamento, data_venda):
        self.cliente = cliente
        self.produto = produto
        self.valor = valor
        self.forma_pagamento = forma_pagamento
        self.status_pagamento = status_pagamento
        self.data_venda = data_venda

class VendasBanco:
    def __init__(self, database):
        self.database = database
        
    def salvar_edicao_vendas(self, editar_vendas_ui):
        # Seu código para salvar a edição aqui
        self.main_window.load_vendas_table()  # Chamando o método load_cliente_table da MainWindow
        
    def insert_vendas(self, vendas):
        try:
            self.database.connect()
            cursor = self.database.connection.cursor()
            cursor.execute(""" 
                INSERT INTO vendas(cliente, produto,valor, forma_pagamento, status_pagamento, data_venda) 
                VALUES (%s, %s, %s, %s, %s)
                """, (
                    vendas.cliente, vendas.produto, vendas.valor, vendas.forma_pagamento, vendas.status_pagamento, 
                    vendas.data_venda
                ))
            self.database.connection.commit()
            print("Venda inserido com sucesso.")
        except mysql.connector.Error as e:
            print("Erro ao inserir Venda:", e)
        finally:
            self.database.close_connection()   
            
class Financeiros: 
    def __init__(self, cliente, produto,valor, valorTotal, forma_pagamento, status_pagamento, data_venda):
        self.cliente = cliente
        self.produto = produto
        self.valor = valor
        self.valorTotal = valorTotal
        self.forma_pagamento = forma_pagamento
        self.status_pagamento = status_pagamento
        self.data_venda = data_venda
        
        
class FinanceirosBanco:
    def __init__(self, database):
        self.database = database
        
    # def salvar_edicao_vendas(self, editar_financeiro_ui):
    #     # Seu código para salvar a edição aqui
    #     self.main_window.load_vendas_table()  # Chamando o método load_cliente_table da MainWindow
        
    def insert_vendas(self, financeiro):
        try:
            self.database.connect()
            cursor = self.database.connection.cursor()
            cursor.execute(""" 
                INSERT INTO financeiro(cliente, produto,valor,valorTotal, forma_pagamento, status_pagamento, data_venda) 
                VALUES (%s, %s, %s, %s, %s)
                """, (
                    financeiro.cliente, financeiro.produto, financeiro.valor,financeiro.valorTotal, financeiro.forma_pagamento, financeiro.status_pagamento, 
                    financeiro.data_venda
                ))
            self.database.connection.commit()
            print("Venda inserido com sucesso.")
        except mysql.connector.Error as e:
            print("Erro ao inserir Venda:", e)
        finally:
            self.database.close_connection()   