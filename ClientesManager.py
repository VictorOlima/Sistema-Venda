from datetime import datetime
from PySide6.QtWidgets import QPushButton, QDialog, QMessageBox, QTableWidgetItem
from interface.editarCliente_ui import Ui_editarCliente
from database import DataBase, Clientes

class ClientesManager:
    def __init__(self, main_window, user_access_level):
        self.main_window = main_window
        self.ui = main_window.ui
        self.db = DataBase()
        self.cliente_codigo = None
        self.user_access_level = user_access_level
    
    def cadastrar_cliente(self, cadastro_cliente, main_window):   
        nome = cadastro_cliente.nome.text()
        rg = cadastro_cliente.rg.text()
        cpf = cadastro_cliente.cpf.text()
        telefone = cadastro_cliente.telefone.text()
        email = cadastro_cliente.email.text()
        endereco = cadastro_cliente.endereco.text()
        data_cadastro = datetime.now()
        
        novo_cliente = Clientes(nome, rg, cpf, telefone, email, endereco, data_cadastro)
        
        self.insert_cliente(novo_cliente)
        
        cadastro_cliente.nome.clear()
        cadastro_cliente.rg.clear()
        cadastro_cliente.cpf.clear()
        cadastro_cliente.telefone.clear()
        cadastro_cliente.email.clear()
        cadastro_cliente.endereco.clear()

    def insert_cliente(self, novo_cliente):
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute(
            "INSERT INTO clientes (nome, rg, cpf, telefone, email, endereco, datacadastro) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (
                novo_cliente.nome,
                novo_cliente.rg,
                novo_cliente.cpf,
                novo_cliente.telefone,
                novo_cliente.email,
                novo_cliente.endereco,
                novo_cliente.datacadastro,
            ),
        )
        self.db.connection.commit()
        self.load_table()
        self.db.close_connection()
        QMessageBox.information(None, "Sucesso", "Cliente cadastrado com sucesso.")

    def load_table(self, cpf_pesquisa=None):
        self.db.connect()
        cursor = self.db.connection.cursor()
        sql_query = "SELECT CODIGO, nome, rg, cpf, telefone, email, endereco, datacadastro FROM clientes"
        if cpf_pesquisa:
            sql_query += f" WHERE cpf LIKE '%{cpf_pesquisa}%' OR nome LIKE '%{cpf_pesquisa}%'"
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        
        self.ui.tabelaClientes.clear()
        header_labels = ["CODIGO", "Nome", "RG", "CPF", "Telefone", "E-Mail", "Endereço", "Data Cadastro", "Ação"]
        
        if self.user_access_level == 'supervisor':
            header_labels.append("Ação")
            
        current_column_count = self.ui.tabelaClientes.columnCount()
        if len(header_labels) > current_column_count:
            self.ui.tabelaClientes.setColumnCount(len(header_labels))
        elif len(header_labels) < current_column_count:
            for i in range(current_column_count - len(header_labels)):
                self.ui.tabelaClientes.removeColumn(len(header_labels))

        self.ui.tabelaClientes.setHorizontalHeaderLabels(header_labels)
        self.ui.tabelaClientes.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.ui.tabelaClientes.setItem(i, j, item)
            btn_editar = QPushButton("Editar")
            btn_editar.clicked.connect(lambda _, i=i: self.editar_cliente(rows[i][0]))
            self.ui.tabelaClientes.setCellWidget(i, len(header_labels) - 1, btn_editar)  # Última coluna é onde o botão "Editar" será inserido
            
            if self.user_access_level == 'supervisor':
                btn_excluir = QPushButton("Excluir")
                btn_excluir.clicked.connect(lambda _, i=i: self.excluir_cliente(rows[i][0]))
                self.ui.tabelaClientes.setCellWidget(i, len(header_labels) - 2, btn_excluir)  # Penúltima coluna é onde o botão "Excluir" será inserido
                
        self.db.close_connection()
    
    def excluir_cliente(self, cliente_codigo):
        reply = QMessageBox.question(None, 'Excluir Cliente', 'Tem certeza que deseja excluir este cliente?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.db.connect()
            cursor = self.db.connection.cursor()
            cursor.execute("DELETE FROM clientes WHERE CODIGO = %s", (cliente_codigo,))
            self.db.connection.commit()
            self.load_table()  # Recarregar a tabela após a exclusão
            self.db.close_connection()
            QMessageBox.information(None, "Sucesso", "Cliente excluído com sucesso.")
    
    def pesquisar_cliente(self, cpf_pesquisa):
        self.load_table(cpf_pesquisa)

    def editar_cliente(self, cliente_codigo):
        self.cliente_codigo = cliente_codigo
        dialog = QDialog()
        editar_cliente_ui = Ui_editarCliente()
        editar_cliente_ui.setupUi(dialog)
        
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT * FROM clientes WHERE CODIGO = %s", (cliente_codigo,))
        cliente = cursor.fetchone()
        if cliente:
            editar_cliente_ui.editarNome.setText(cliente[1])
            editar_cliente_ui.editarRg.setText(cliente[2])
            editar_cliente_ui.editarCpf.setText(cliente[3])
            editar_cliente_ui.editarTelefone.setText(cliente[4])
            editar_cliente_ui.editarEmail.setText(cliente[5])
            editar_cliente_ui.editarEndereco.setText(cliente[6])

            editar_cliente_ui.botaoEditar.clicked.connect(lambda: self.salvar_edicao_cliente(editar_cliente_ui))

            if dialog.exec() == QDialog.Accepted:
                novo_nome = editar_cliente_ui.editarNome.text()
                novo_rg = editar_cliente_ui.editarRg.text()
                novo_cpf = editar_cliente_ui.editarCpf.text()
                novo_telefone = editar_cliente_ui.editarTelefone.text()
                novo_email = editar_cliente_ui.editarEmail.text()
                novo_endereco = editar_cliente_ui.editarEndereco.text()
                
                datacadastro = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                cursor.execute(
                    "UPDATE clientes SET nome = %s, rg = %s, cpf = %s, telefone = %s, email = %s, endereco = %s, datacadastro = %s WHERE CODIGO = %s",
                    (
                        novo_nome,
                        novo_rg,
                        novo_cpf,
                        novo_telefone,
                        novo_email,
                        novo_endereco,
                        datacadastro,
                        cliente_codigo
                    ),
                )
                self.db.connection.commit()
                self.load_table()
        else:
            print(f"Cliente com ID {cliente_codigo} não encontrado")

        self.db.close_connection()

    def salvar_edicao_cliente(self, ui_editarCliente):
        novo_nome = ui_editarCliente.editarNome.text()
        novo_rg = ui_editarCliente.editarRg.text()
        novo_cpf = ui_editarCliente.editarCpf.text()
        novo_telefone = ui_editarCliente.editarTelefone.text()
        novo_email = ui_editarCliente.editarEmail.text()
        novo_endereco = ui_editarCliente.editarEndereco.text()

        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute(
            "UPDATE clientes SET nome = %s, rg = %s, cpf = %s, telefone = %s,  email = %s, endereco = %s, datacadastro = %s WHERE CODIGO = %s",
            (
                novo_nome,
                novo_rg,
                novo_cpf,
                novo_telefone,
                novo_email,
                novo_endereco,
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                self.cliente_codigo
            ),
        )
        self.db.connection.commit()
        self.load_table()
        self.db.close_connection()
