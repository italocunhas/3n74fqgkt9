from PyQt5 import uic, QtWidgets
import mysql.connector

conexao = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '1234',
    database = 'credito'
)
def inserir_dados():
    nome = cadastros.txtNome.text()
    cpf = cadastros.txtCpf.text()
    idade = cadastros.txtIdade.text()
    renda = cadastros.txtRenda.text()
    situacao = cadastros.txtSituacao.text()

    cursor = conexao.cursor()
    comando_SQL = 'insert into clientes (nome,cpf,idade,renda,situacao) values(%s,%s,%s,%s,%s)'
    dados = (str(nome),str(cpf),str(idade),str(renda),str(situacao))
    cursor.execute(comando_SQL, dados)

    conexao.commit()
    
    cadastros.txtNome.setText('')
    cadastros.txtCpf.sextText('')
    cadastros.txtIdade.setText('')
    cadastros.txtRenda.sextText('')
    cadastros.txtSituacao.setText('')
    cadastros.lblAnalise.setText('Clique no Botão "Analisar Crédito"')
def analise():
    renda = cadastros.txtRenda.text()
    renda = float(renda)
    idade = cadastros.txtIdade.text()
    idade = float(idade)
    
    if renda>=3500 and idade >=21:
        cadastros.lblAnalise.setText('Cadastro com chances de crédito')
    else:
        cadastros.lblAnalise.setText('Cadastro não selecionado para crédito')

def relatorio():
    relatorio.show() 
    
    cursor = conexao.cursor()
    comando_SQL = 'select * from clientes'
    cursor.execute(comando_SQL)
    
app=QtWidgets.QApplication([])
cadastros=uic.loadUi('cadastros.ui')
cadastros.btnSalvar.clicked.connect(inserir_dados)
cadastros.btnAnalise.clicked.connect(analise)
cadastros.btnRelatorio.clicked.connect(relatorio)

relatorio=uic.loadUi('relatorio.ui')

    

cadastros.show()
app.exec()