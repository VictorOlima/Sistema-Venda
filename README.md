# Sistema Venda

Sistema de venda é uma aplicação destinada a desktop, para fins de apresentação de trabalho para faculdade UNIP-EAD, curso Analise e desenvolvimento de Sistema.

O sistema foi desenvolvido para gerenciar as vendas de uma empresa.

# Tema
Levantamento e análise de requisitos de um sistema de controle de vendas de uma loja de jogos, acessórios e produtos geek.

## Objetivos específicos

Os seguintes aspectos devem ser considerados: 
- Todo acesso ao sistema é feito na loja por meio de login e senha; 
- O estoquista cadastra os produtos que serão vendidos na loja e que deverão ser divididos por categorias: jogos, acessórios e produtos geek; 
- Os cadastros dos clientes devem possuir: código, RG, CPF, nome, data do cadastro, endereço, telefone e e-mail do cliente; 
- Todos os produtos devem possuir: código de barras, nome do produto, categoria, fabricante, quantidade e valor do produto. 
- Para os jogos e acessórios, devem ser informados em qual plataforma serão utilizados e qual o prazo de garantia que o produto possui; 
- A venda deverá possuir os dados do cliente e todos os produtos adquiridos. Deve ser gerado um código único da venda, com a data da venda, o valor da venda, opções para pagamento (dinheiro/cartão), status de pagamento e status da venda; 
- O atendente poderá excluir produtos da venda caso o cliente não queira mais adquiri lós. Apenas o supervisor da loja poderá excluir o produto da venda, devendo informar um usuário e senha válidos; 
- O atendente poderá consultar os preços dos produtos caso o cliente solicite; A venda pode ser cancelada apenas pelo supervisor da loja, que deve informar usuário e senha válidos. No momento do cancelamento, o código da venda deve ser enviado para o sistema financeiro.

## Layout desktop

![Layout desktop](https://github.com/VictorOlima/Sistema-Venda/blob/main/assets/Login.png)
![Layout desktop](https://github.com/VictorOlima/Sistema-Venda/blob/main/assets/vendas.png)
![Layout desktop](https://github.com/VictorOlima/Sistema-Venda/blob/main/assets/usuario.png)

# Tecnologias utilizadas

## Back end

Python
PySide6
MySql

## Implantação em produção

- Financeiro, modificar modelo para mostrar gráfico e valor total, e integrar a pesquisa.
- Botões de menu, integrar funcionalidade ao click, Fazer Logout.
- Fazer função para, se supervisor estiver utilizando sistema, não pedir senha para deletar vendas.
- Função estoquista, pode somente adicionar produtos.
- Formatar datas.

Aceito melhorias em meu projeto.

# Autor
Victor Lima
https://www.linkedin.com/in/victor-henrique-301802181/