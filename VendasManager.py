from datetime import datetime
from PySide6.QtWidgets import QDialog, QTableWidgetItem, QPushButton, QMessageBox,QLineEdit,QVBoxLayout,QLabel
from database import DataBase, Vendas
from interface.editarVendas_ui import Ui_editarVendas
import locale
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Supervisor")
        layout = QVBoxLayout()
        self.label_login = QLabel("Login:")
        self.edit_login = QLineEdit()
        layout.addWidget(self.label_login)
        layout.addWidget(self.edit_login)

        self.label_senha = QLabel("Senha:")
        self.edit_senha = QLineEdit()
        self.edit_senha.setEchoMode(QLineEdit.EchoMode.Password)  # Para ocultar a senha
        layout.addWidget(self.label_senha)
        layout.addWidget(self.edit_senha)

        self.btn_login = QPushButton("Login")
        self.btn_login.clicked.connect(self.accept)  # Aceita a entrada quando o botão é clicado
        layout.addWidget(self.btn_login)

        self.setLayout(layout)
        
    def get_login_senha(self):
        return self.edit_login.text(), self.edit_senha.text()   

class VendasManager:
    def __init__(self, main_window):
        self.main_window = main_window
        self.ui = main_window.ui
        self.db = DataBase()
        self.vendas_codigo = None

    def buscar_clientes(self, nome_clientes):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT nome FROM clientes WHERE nome LIKE %s", ('%' + nome_clientes + '%',))
        Clientes = cursor.fetchall()
        self.db.close_connection()
        nomes_clientes = [cliente[0] for cliente in Clientes]
        return nomes_clientes

    def listar_todos_clientes(self):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT nome FROM clientes")
        clientes = cursor.fetchall()
        self.db.close_connection()
        nomes_clientes = [cliente[0] for cliente in clientes]
        return nomes_clientes

    def buscar_produtos(self, nome_produto):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT nome FROM produtos WHERE nome LIKE %s", ('%' + nome_produto + '%',))
        produtos = cursor.fetchall()
        self.db.close_connection()
        nomes_produtos = [produto[0] for produto in produtos]
        return nomes_produtos

    def listar_todos_produtos(self):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT nome FROM produtos")
        produtos = cursor.fetchall()
        self.db.close_connection()
        nomes_produtos = [produto[0] for produto in produtos]
        return nomes_produtos

    def get_valor_produto(self, nome_produto):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT valor FROM produtos WHERE nome = %s", (nome_produto,))
        produto = cursor.fetchone()
        self.db.close_connection()
        return produto[0] if produto else None

    def update_valor_produto(self, nome_produto, cadastro_vendas):
        valor_produto = self.get_valor_produto(nome_produto)
        if valor_produto is not None:
            cadastro_vendas.vendasValor.setText(str(valor_produto))

    def cadastrar_vendas(self, cadastro_vendas):
        cliente = cadastro_vendas.vendasCliente.text()
        produto_nome = cadastro_vendas.vendasProdutos.text()
        forma_pagamento = cadastro_vendas.vendasPagamento.text()
        status_pagamento = cadastro_vendas.vendasStatus.text()

        # Formatar a data da venda no formato "Dia Mês Ano"
        data_venda = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Usar o valor atual do campo de valor, seja ele editado ou não
        valor_produto = cadastro_vendas.vendasValor.text()
        
        if produto_nome:
            quantidade_disponivel = self.get_quantidade_produto(produto_nome)

            if quantidade_disponivel > 0:
                nova_quantidade = quantidade_disponivel - 1
                self.update_quantidade_produto(produto_nome, nova_quantidade)
            else:
                QMessageBox.warning(None, "Erro", "Produto esgotado.")
                return
        else:
            QMessageBox.warning(None, "Erro", "Produto não encontrado no banco de dados.")
            return

        nova_venda = Vendas(cliente, produto_nome, float(valor_produto), forma_pagamento, status_pagamento, data_venda)
        self.insert_vendas(nova_venda)

        # Limpar os campos após a inserção bem-sucedida, se necessário
        cadastro_vendas.vendasCliente.clear()
        cadastro_vendas.vendasProdutos.clear()
        cadastro_vendas.vendasValor.clear()
        cadastro_vendas.vendasPagamento.clear()
        cadastro_vendas.vendasStatus.clear()

    def get_quantidade_produto(self, nome_produto):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT quantidade FROM produtos WHERE nome = %s", (nome_produto,))
        produto = cursor.fetchone()
        self.db.close_connection()
        return produto[0] if produto else 0

    def update_quantidade_produto(self, nome_produto, nova_quantidade):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute("UPDATE produtos SET quantidade = %s WHERE nome = %s", (nova_quantidade, nome_produto))
        self.db.connection.commit()
        self.db.close_connection()
        
    def insert_vendas(self, nova_venda):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute(
            "INSERT INTO vendas (cliente, produto, valor, forma_pagamento, status_pagamento, data_venda) VALUES (%s, %s, %s, %s, %s, %s)",
            (
                nova_venda.cliente,
                nova_venda.produto,
                nova_venda.valor,
                nova_venda.forma_pagamento,
                nova_venda.status_pagamento,
                nova_venda.data_venda,
            ),
        )
        self.db.connection.commit()
        self.load_table()
        self.db.close_connection()
        QMessageBox.information(None, "Sucesso", "Cliente cadastrado com sucesso.")

    def load_table(self, vendas_pesquisa=None):
        self.db.connect()
        cursor = self.db.connection.cursor()
        sql_query = "SELECT ID, cliente, produto, valor, forma_pagamento, status_pagamento, data_venda FROM vendas"
        if vendas_pesquisa:
            sql_query += f" WHERE id LIKE '%{vendas_pesquisa}%' OR cliente LIKE '%{vendas_pesquisa}%'"
        cursor.execute(sql_query)
        rows = cursor.fetchall()

        self.ui.tabelaVendas.clear()
        self.ui.tabelaVendas.setColumnCount(9)
        self.ui.tabelaVendas.setHorizontalHeaderLabels(
            [
                "CODIGO",
                "Cliente",
                "Produto",
                "Valor",
                "Forma de Pagamento",
                "Status Pagamento",
                "Data venda",
                "Ação",
                "Ação"
            ]
        )
        self.ui.tabelaVendas.setRowCount(len(rows))

        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                if j == 6:  # Coluna de data
                    if isinstance(col, datetime):  # Verifica se já é um objeto datetime
                        col = col.strftime("%d/%m/%Y %H:%M:%S")
                    else:  # Caso contrário, converte a string para datetime primeiro
                        col = datetime.strptime(col, "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y %H:%M:%S")
                item = QTableWidgetItem(str(col))
                self.ui.tabelaVendas.setItem(i, j, item)
            btn_editar = QPushButton("Editar")
            btn_editar.clicked.connect(lambda _, i=i: self.editar_vendas(rows[i][0]))
            self.ui.tabelaVendas.setCellWidget(i, 7, btn_editar)
            
            btn_excluir = QPushButton("Excluir")
            btn_excluir.clicked.connect(lambda _, i=i: self.excluir_vendas(rows[i][0]))
            self.ui.tabelaVendas.setCellWidget(i, 8, btn_excluir) # Penúltima coluna é onde o botão "Excluir" será inserido

        self.db.close_connection()
  
    def excluir_vendas(self, vendas_id):
        dialog = LoginDialog()
        if dialog.exec() == QDialog.Accepted:
            login, senha = dialog.get_login_senha()
            if not self.autenticar_supervisor(login, senha):
                QMessageBox.warning(None, "Aviso", "Somente supervisores podem excluir vendas.")
                return

            reply = QMessageBox.question(None, 'Excluir Vendas', 'Tem certeza que deseja excluir esta venda?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.db.connect()
                cursor = self.db.connection.cursor()
                cursor.execute("DELETE FROM vendas WHERE id = %s", (vendas_id,))
                self.db.connection.commit()
                self.load_table()  # Recarregar a tabela após a exclusão
                self.db.close_connection()
                QMessageBox.information(None, "Sucesso", "Venda excluída com sucesso.")
        
    def validar_credenciais(self):
        login = self.login_edit.text()
        senha = self.senha_edit.text()
        if not self.autenticar_supervisor(login, senha):
            self.accept()
        else:
            self.message_label.setText("Credenciais inválidas")

    def autenticar_supervisor(self, login, senha):
        return login == "admin" and senha == "admin"

    def pesquisar_vendas(self, vendas_pesquisa):
        self.load_table(vendas_pesquisa)

    def editar_vendas(self, vendas_codigo):
        self.vendas_codigo = vendas_codigo
        dialog = QDialog()
        editar_vendas_ui = Ui_editarVendas()
        editar_vendas_ui.setupUi(dialog)

        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT * FROM vendas WHERE ID = %s", (vendas_codigo,))
        venda = cursor.fetchone()
        if venda:
            editar_vendas_ui.editarVendasCliente.setText(venda[1])
            editar_vendas_ui.editarVendasProdutos.setText(venda[2])
            editar_vendas_ui.editarVendasValor.setText(str(venda[3]))
            editar_vendas_ui.editarVendasPagamento.setText(venda[4])
            editar_vendas_ui.editarVendasStatus.setText(venda[5])

            # Conectar o botão de "Salvar" à função de salvar edição
            editar_vendas_ui.cadastrarVenda.clicked.connect(lambda: self.salvar_edicao_vendas(editar_vendas_ui))

            if dialog.exec() == QDialog.Accepted:
                novo_cliente = editar_vendas_ui.editarVendasCliente.text()
                novo_produto = editar_vendas_ui.editarVendasProdutos.text()
                novo_valor = editar_vendas_ui.editarVendasValor.text()
                novo_pagamento = editar_vendas_ui.editarVendasPagamento.text()
                novo_status = editar_vendas_ui.editarVendasStatus.text()

                data_venda = datetime.now().strftime("%d %B %Y")

                cursor.execute(
                    "UPDATE vendas SET cliente = %s, produto = %s, valor = %s, forma_pagamento = %s, status_pagamento = %s, data_venda = %s WHERE ID = %s",
                    (
                        novo_cliente,
                        novo_produto,
                        novo_valor,
                        novo_pagamento,
                        novo_status,
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        self.vendas_codigo,
                    ),
                )
                self.db.connection.commit()
                self.load_table()
        else:
            print(f"Venda com ID {vendas_codigo} não encontrado")

        self.db.close_connection()

    def salvar_edicao_vendas(self, editar_vendas_ui):
        novo_cliente = editar_vendas_ui.editarVendasCliente.text()
        novo_produto = editar_vendas_ui.editarVendasProdutos.text()
        novo_valor = editar_vendas_ui.editarVendasValor.text()
        novo_pagamento = editar_vendas_ui.editarVendasPagamento.text()
        novo_status = editar_vendas_ui.editarVendasStatus.text()
        # Realizar a lógica de validação dos campos, se necessário

        # Executar a atualização no banco de dados
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute(
            "UPDATE vendas SET cliente = %s, produto = %s, valor = %s, forma_pagamento = %s, status_pagamento = %s, data_venda = %s WHERE ID = %s",
            (
                novo_cliente,
                novo_produto,
                novo_valor,
                novo_pagamento,
                novo_status,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                self.vendas_codigo,
            ),
        )
        self.db.connection.commit()
        self.load_table()
        self.db.close_connection()
        QMessageBox.information(None, "Sucesso", "Venda atualizada com sucesso.")