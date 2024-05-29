import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox,QCompleter
from interface.cadastroCliente_ui import Ui_cadastroCliente
from interface.login_ui import Ui_Login
from interface.main_ui import Ui_MainWindow
from VendasManager import VendasManager
from ClientesManager import ClientesManager
from ProdutoManager import ProdutosManager
from FinanceiroManager import FinanceiroManager
from interface.cadastrarVendas_ui import Ui_cadastroVendas
from interface.cadastroProdutos_ui import Ui_cadastroProdutos
from database import DataBase, UserManager, User

class MainWindow(QMainWindow):
       
    def __init__(self, user_manager, user_access_level):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Sistema")
        self.user_manager = user_manager
        self.user_access_level = user_access_level
        
        self.ui.label.setText(f"Usuário: {user_access_level}")
        
        self.ui.clientes_2.clicked.connect(self.switch_to_clientes)
        self.ui.vendas_2.clicked.connect(self.switch_to_vendas)
        self.ui.produtos_2.clicked.connect(self.switch_to_produtos)
        self.ui.finandeiro_2.clicked.connect(self.switch_to_financeiro)
        self.ui.config_2.clicked.connect(self.switch_to_config)
        self.ui.pesquisarClientes.clicked.connect(self.pesquisar_cliente)
        self.ui.pesquisarVendas.clicked.connect(self.pesquisar_vendas)
        self.ui.pesquisarProdutos.clicked.connect(self.pesquisar_produtos)
        self.ui.clientesCadastrar.clicked.connect(self.load_cliente_cadastrar)
        self.ui.adicionarVendas.clicked.connect(self.load_vendas_cadastrar)
        self.ui.cadastrarProdutos.clicked.connect(self.load_produtos_cadastrar)
        self.ui.cadastrarUsuario.clicked.connect(self.cadastrar_usuario)
        self.ui.inputClientes.textChanged.connect(self.pesquisar_cliente)
        self.ui.inputVendas.textChanged.connect(self.pesquisar_vendas)
        self.ui.inputProdutos.textChanged.connect(self.pesquisar_produtos)
        
                
        self.cliente_manager = ClientesManager(self, user_access_level)  # Passando a instância da MainWindow para o ClienteManager
        self.produtos_manager = ProdutosManager(self)
        self.vendas_manager = VendasManager(self)
        self.financeiro_manager = FinanceiroManager(self)
        self.load_cliente_table()
        self.load_produto_table()
        self.load_financeiro_table()
        self.load_vendas_table()
        self.hide_inappropriate_menus()

    def hide_inappropriate_menus(self):
        if self.user_access_level != "supervisor":
            self.ui.config_2.hide()  # Esconde o menu de configurações para usuários não administradores
            self.ui.finandeiro_2.hide()
            self.ui.label.setText(f"Usuário: {self.user_access_level}")
            
    def cadastrar_usuario(self):
        nome = self.ui.nomeUsuario.text()
        user = self.ui.usuario.text()
        senha = self.ui.senha_1.text()
        perfil = self.ui.perfil.currentText()

        if nome and user and senha and perfil:
            novo_usuario = User(nome, user, senha, perfil)
            self.user_manager.insert_user(novo_usuario)
            
            QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso.")
            
            self.clear_fields()
        else:
            QMessageBox.warning(self, "Cadastro de Usuário", "Por favor, preencha todos os campos.")

    def setup_vendas_ui(self):
        self.ui_vendas = Ui_cadastroVendas()
        self.ui_vendas.setupUi(self.vendas)
        self.ui_vendas.cadastrarVenda.clicked.connect(lambda: self.vendas_manager.cadastrar_venda(self.ui_vendas, self))

    def clear_fields(self):

        self.ui.nomeUsuario.setText("")
        self.ui.usuario.setText("")
        self.ui.senha_1.setText("")
        self.ui.senha_2.setText("")
        self.ui.perfil.setCurrentIndex(0)
        
    def switch_to_clientes(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def switch_to_vendas(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def switch_to_produtos(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.load_produto_table()

    def switch_to_financeiro(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.load_financeiro_table()

    def switch_to_config(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        
    def pesquisar_cliente(self):
        cpf_pesquisar = self.ui.inputClientes.text()
        self.cliente_manager.pesquisar_cliente(cpf_pesquisar)
        
    def pesquisar_vendas(self):
        vendas_pesquisa = self.ui.inputVendas.text()
        self.vendas_manager.pesquisar_vendas(vendas_pesquisa)
        
    def pesquisar_produtos(self):
        nome_pesquisa = self.ui.inputProdutos.text()
        self.produtos_manager.pesquisar_produtos(nome_pesquisa)

    def load_produto_table(self):
        # Chama a função load_table sem argumentos para carregar todos os clientes
        self.produtos_manager.load_table_produtos()
        
    def load_financeiro_table(self):
        self.financeiro_manager.load_table_financeiro()
        
    def load_cliente_table(self):
        # Chama a função load_table sem argumentos para carregar todos os clientes
        self.cliente_manager.load_table()   
        
    def load_vendas_table(self):
        # Chama a função load_table sem argumentos para carregar todos os vendas
        self.vendas_manager.load_table()   
        
    def load_produtos_cadastrar(self):
        dialog = QDialog()
        cadastro_produtos = Ui_cadastroProdutos()
        cadastro_produtos.setupUi(dialog)
        # Modifique a linha abaixo para passar a instância de MainWindow corretamente
        cadastro_produtos.btnCadastrarProdutos.clicked.connect(lambda: self.produtos_manager.cadastrar_produtos(cadastro_produtos))

        dialog.exec()    
        
    def load_cliente_cadastrar(self):
        dialog = QDialog()
        cadastro_cliente = Ui_cadastroCliente()
        cadastro_cliente.setupUi(dialog)
        # Modifique a linha abaixo para passar a instância de MainWindow corretamente
        cadastro_cliente.btnCadastrarCliente.clicked.connect(lambda: self.cliente_manager.cadastrar_cliente(cadastro_cliente, self))
        dialog.exec()
        
    def load_vendas_cadastrar(self):
        dialog = QDialog()
        cadastro_vendas = Ui_cadastroVendas()
        cadastro_vendas.setupUi(dialog)
        
        
        clientes = self.vendas_manager.listar_todos_clientes()
        completer = QCompleter(clientes)
        cadastro_vendas.vendasCliente.setCompleter(completer)
        
        # Buscar todos os produtos e configurar o QCompleter
        produtos = self.vendas_manager.listar_todos_produtos()
        completer = QCompleter(produtos)
        cadastro_vendas.vendasProdutos.setCompleter(completer)
        
        # Conectar o sinal activated do QCompleter ao método update_valor_produto
        completer.activated.connect(lambda text: self.vendas_manager.update_valor_produto(text, cadastro_vendas))
        
        # Conectar o botão de cadastrar vendas
        cadastro_vendas.cadastrarVenda.clicked.connect(lambda: self.vendas_manager.cadastrar_vendas(cadastro_vendas))
        
        dialog.exec()
        
    def salvar_edicao_cliente(self, ui_editarCliente):
        # Seu código para salvar a edição aqui
        self.main_window.load_cliente_table()  # Chamando o método load_produto_table da MainWindow
         
    def salvar_edicao(self, ui_editarProdutos):
        # Seu código para salvar a edição aqui
        self.main_window.load_produto_table()  # Chamando o método load_produto_table da MainWindow
   
class LoginWindow(QMainWindow):
    
    def __init__(self, user_manager):
        super(LoginWindow, self).__init__()
        self.tentativas = 0
        self.user_manager = user_manager
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.setWindowTitle("Login")
        self.ui.btn_entrar.clicked.connect(self.check_login)
        self.ui.inputSenha.returnPressed.connect(self.ui.btn_entrar.click)

    def check_login(self):
        autenticado = self.user_manager.check_user(
            self.ui.inputNome.text().upper(), self.ui.inputSenha.text()
        )
        if autenticado is not None:
            self.hide()
            main_window = MainWindow(self.user_manager, autenticado)  # Não chame .lower() aqui
            main_window.show()
        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(
                    f"Login ou senha incorreto \n\n Tentativa: {self.tentativas + 1} de 3"
                )
                msg.exec()
                self.tentativas += 1
            if self.tentativas == 3:
                self.user_manager.database.close_connection()
                sys.exit(0)
     
if __name__ == "__main__":
    db = DataBase()
    db.create_database()
    app = QApplication(sys.argv)
    db.create_table_users()
    db.create_table_clientes()
    db.create_table_produtos()
    db.create_table_vendas()
    db.create_table_financeiro()
    user_manager = UserManager(db)
    login_window = LoginWindow(user_manager)
    login_window.show()
    sys.exit(app.exec())