from datetime import datetime
import random
from PySide6.QtWidgets import QPushButton, QDialog, QMessageBox, QTableWidgetItem
from database import DataBase, Produtos
from interface.editarProdutos_ui import Ui_editarProdutos

class ProdutosManager:
    def __init__(self, main_window):
        self.main_window = main_window
        self.ui = main_window.ui  # Acessando a instância do Ui_MainWindow da MainWindow
        self.db = DataBase()
        self.produto_codigo = None
        
        
    def generate_barcode(self, categoria):
        # Gerar um código de barras aleatório baseado na categoria
        if categoria == "Jogos":
            return str(random.randint(1000000,1999999))
        elif categoria == "Acessórios":
            return str(random.randint(2000000,2999999))
        elif categoria == "Produtos Geek":
            return str(random.randint(3000000,4999999))
        else:
            # Se a categoria não estiver mapeada, gerar um código de barras aleatório
            return str(random.randint(5000000, 9999999))    
        
    def is_numeric(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False        
        
    def cadastrar_produtos(self, cadastro_produtos):
        # Obter os valores dos campos do formulário   
        nome = cadastro_produtos.nome.text()
        categoria = cadastro_produtos.categoria.currentText()
        fabricante = cadastro_produtos.fabricante.text()
        quantidade = cadastro_produtos.quantidade.text()
        garantia = cadastro_produtos.garantia.text()
        valor = cadastro_produtos.valor.text()

        
        # Gerar o código de barras com base na categoria
        codigoDeBarra = self.generate_barcode(categoria)
        
        # Verificar se todos os campos obrigatórios estão preenchidos
        if nome and categoria and fabricante:
            if self.is_numeric(quantidade) and self.is_numeric(valor) and self.is_numeric(codigoDeBarra):
                # Criar um novo objeto Produtos com os dados do formulário
                novo_produtos = Produtos(nome, categoria, fabricante, quantidade,garantia, valor, codigoDeBarra)
                
                # Inserir os dados no banco de dados
                self.insert_produtos(novo_produtos)
                
                # Carregar novamente a tabela de produtos para refletir as mudanças
                self.load_table_produtos()
                
                # Limpar os campos do formulário após a inserção bem-sucedida
                cadastro_produtos.nome.clear()
                cadastro_produtos.fabricante.clear()
                cadastro_produtos.quantidade.clear()
                cadastro_produtos.garantia.clear()  
                cadastro_produtos.valor.clear()
                cadastro_produtos.codigoDeBarra.clear()
            else:
                QMessageBox.warning(None, "Erro", "Os campos de quantidade, valor e código de barras devem ser numéricos.")
        else:
            QMessageBox.warning(None, "Erro", "Por favor, preencha todos os campos obrigatórios.")

    def insert_produtos(self, novo_produtos):
        self.db.connect()
        cursor = self.db.connection.cursor()

        # Verifica se o código de barras já existe no banco de dados
        cursor.execute("SELECT codigoDeBarra FROM produtos WHERE codigoDeBarra = %s", (novo_produtos.codigoDeBarra,))
        existing_product = cursor.fetchone()

        if existing_product:
            QMessageBox.warning(None, "Erro", "O código de barras já está em uso.")
        else:
            cursor.execute(
                "INSERT INTO produtos (nome, categoria, fabricante, quantidade, garantia, valor , codigoDeBarra) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (
                    novo_produtos.nome,
                    novo_produtos.categoria,
                    novo_produtos.fabricante,
                    novo_produtos.quantidade,
                    novo_produtos.garantia,
                    novo_produtos.valor,
                    novo_produtos.codigoDeBarra,
                ),
            )
            self.db.connection.commit()
            self.load_table_produtos()  # Carrega a tabela de produtos novamente após a inserção
            QMessageBox.information(None, "Sucesso", "Produto cadastrado com sucesso.")

        self.db.close_connection()
        
    def load_table_produtos(self, nome_pesquisa=None):
        self.db.connect()
        cursor = self.db.connection.cursor()
        sql_query = "SELECT CODIGO, nome, categoria, fabricante, quantidade, garantia, valor, codigoDeBarra FROM produtos"
        if nome_pesquisa:
            sql_query += f" WHERE categoria LIKE '%{nome_pesquisa}%' OR nome LIKE '%{nome_pesquisa}%'"
        cursor.execute(sql_query)
        rows = cursor.fetchall()
    

        self.ui.tabelaProduto.clear()
        self.ui.tabelaProduto.setHorizontalHeaderLabels(
            [
                "CODIGO",
                "Nome",
                "Categoria",
                "Fabricante",
                "Quantidade",
                "Garantia",
                "Valor",
                "Código de Barras",
                "Editar"
            ]
        )
        self.ui.tabelaProduto.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.ui.tabelaProduto.setItem(i, j, item)
            btn_editar = QPushButton("Editar")
            btn_editar.clicked.connect(lambda _, i=i: self.editar_produtos(rows[i][0]))
            self.ui.tabelaProduto.setCellWidget(i, 8, btn_editar)

        self.db.close_connection()

    def pesquisar_produtos(self, nome_pesquisa):
        self.load_table_produtos(nome_pesquisa)

    def editar_produtos(self, produto_codigo):
        self.produto_codigo = produto_codigo
        dialog = QDialog()
        ui_editarProdutos = Ui_editarProdutos()
        ui_editarProdutos.setupUi(dialog)

        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT * FROM produtos WHERE CODIGO = %s", (produto_codigo,))
        produtos = cursor.fetchone()
        if produtos:
            ui_editarProdutos.editarNome.setText(produtos[1])
            ui_editarProdutos.editarCategoria.setCurrentText(produtos[2])
            ui_editarProdutos.editarFabrincante.setText(produtos[3])
            ui_editarProdutos.editarQuantidade.setText(str(produtos[4]))
            ui_editarProdutos.EditarGarantia.setText(produtos[5])
            ui_editarProdutos.editarValor.setText(str(produtos[6]))
            ui_editarProdutos.EditarCodigoDeBarra.setText(produtos[7])

            # Conectar o botão de "Salvar" à função de salvar edição
            ui_editarProdutos.btnEditarProdutos.clicked.connect(lambda: self.salvar_edicao(ui_editarProdutos))

            if dialog.exec() == QDialog.Accepted:
                # Lógica de edição do diálogo aqui
                pass
        else:
            print(f"Produto com ID {produto_codigo} não encontrado")

        self.db.close_connection()

    def salvar_edicao(self, ui_editarProdutos):
        novo_nome = ui_editarProdutos.editarNome.text()
        novo_categoria = ui_editarProdutos.editarCategoria.currentText()
        novo_fabricante = ui_editarProdutos.editarFabrincante.text()
        novo_quantidade = ui_editarProdutos.editarQuantidade.text()
        novo_garantia = ui_editarProdutos.EditarGarantia.text()
        novo_valor = ui_editarProdutos.editarValor.text()
        novo_codigoDeBarra = ui_editarProdutos.EditarCodigoDeBarra.text()

        # Realizar a lógica de validação dos campos, se necessário

        # Executar a atualização no banco de dados
        self.db.connect()
        cursor = self.db.connection.cursor()
        cursor.execute(
            "UPDATE produtos SET nome = %s, categoria = %s, fabricante = %s, quantidade = %s,  garantia = %s, valor = %s, codigoDeBarra = %s WHERE CODIGO = %s",
            (
                novo_nome,
                novo_categoria,
                novo_fabricante,
                novo_quantidade,
                novo_garantia,
                novo_valor,
                novo_codigoDeBarra,
                self.produto_codigo
            ),
        )
        self.db.connection.commit()
        self.load_table_produtos()   # Carregar novamente a tabela após a atualização
        self.db.close_connection()