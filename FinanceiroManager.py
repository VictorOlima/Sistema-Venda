from datetime import datetime
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem
from database import DataBase
import locale
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

class FinanceiroManager:
    def __init__(self, main_window):
        self.main_window = main_window
        self.ui = main_window.ui
        self.db = DataBase()
        self.vendas_codigo = None

    def load_table_financeiro(self, financeiro_pesquisa=None):
        self.db.connect()
        cursor = self.db.connection.cursor()
        
        sql_query = """
        SELECT ID, cliente, produto, valor, forma_pagamento, status_pagamento, data_venda 
        FROM vendas 
        WHERE status_pagamento = 'pago'
        """
        
        if financeiro_pesquisa:
            sql_query += f" AND (id LIKE '%{financeiro_pesquisa}%' OR cliente LIKE '%{financeiro_pesquisa}%')"
        
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        self.ui.tabelaFinanceiro.clearContents()
        self.ui.tabelaFinanceiro.setRowCount(0)
        self.ui.tabelaFinanceiro.setColumnCount(8)
        self.ui.tabelaFinanceiro.setHorizontalHeaderLabels([
            "CODIGO",
            "Cliente",
            "Produto",
            "Valor",
            "Forma de Pagamento",
            "Status Pagamento",
            "Data venda",
            "Valor Total"
        ])
        self.ui.tabelaFinanceiro.setRowCount(len(rows) + 1)  # Adiciona uma linha extra para o total

        total_valor = 0.0  # Variável para armazenar a soma dos valores

        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                if j == 6:
                    if isinstance(col, datetime):
                        col = col.strftime("%d/%m/%Y %H:%M:%S")
                    else:
                        col = datetime.strptime(col, "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y %H:%M:%S")
                item = QTableWidgetItem(str(col))
                self.ui.tabelaFinanceiro.setItem(i, j, item)
                if j == 3:  # Coluna "valor"
                    total_valor += float(col)  # Somar os valores

        # Adicionar a linha com o total das vendas pagas
        total_row_index = len(rows)
        total_label_item = QTableWidgetItem("Total")
        total_label_item.setFlags(total_label_item.flags() ^ Qt.ItemIsEditable)  # Tornar a célula não editável
        self.ui.tabelaFinanceiro.setItem(total_row_index, 0, total_label_item)

        total_value_item = QTableWidgetItem(f"R$ {total_valor:.2f}")
        total_value_item.setFlags(total_value_item.flags() ^ Qt.ItemIsEditable)  # Tornar a célula não editável
        self.ui.tabelaFinanceiro.setItem(total_row_index, 7, total_value_item)

        self.db.close_connection()
