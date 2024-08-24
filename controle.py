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
    leitura_clientes = cursor.fetchall()
    
    relatorio.tableClientes.setRowCount(len(leitura_clientes))
    relatorio.tableClientes.setColumnCount(6)
    
    for i in range (0, len(leitura_clientes)):
        for j in range(0, 6):
            relatorio.tableClientes.setItem(i, j, QtWidgets.QTableWidgetItem(str(leitura_clientes[i][j])))
            
numero_id_geral = 0 
def editar_dados():
    global numero_id_geral
    dados = relatorio.tableClientes.currentRow()
    cursor = conexao.cursor()
    cursor.execute('select id from clientes')
    leitura_clientes = cursor.fetchall()
    id_ativo = leitura_clientes [dados] [0]
    cursor.execute('select * from clientes where id='+str(id_ativo))
    leitura_clientes = cursor.fetchall()
        
    editar.show()
    numero_id_geral = id_ativo
    
    editar.txtAlterarId.setText(str(leitura_clientes[0][0]))
    editar.txtAlterarNome.setText(str(leitura_clientes[0][1]))
    editar.txtAlterarCPF.setText(str(leitura_clientes[0][2]))
    editar.txtAlterarIdade.setText(str(leitura_clientes[0][3]))
    editar.txtAlterarRenda.setText(str(leitura_clientes[0][4]))
    editar.txtAlterarSituacao.setText(str(leitura_clientes[0][5]))
    
def alteracao_de_dados():
    global numero_id_geral
    
    id = editar.txtAlterarId.text()
    nome = editar.txtAlterarNome.text()
    cpf = editar.txtAlterarCPF.text()
    idade = editar.txtAlterarIdade.text()
    renda = editar.txtAlterarRenda.text()
    situacao = editar.txtAlterarSituacao.text()
    
    cursor = conexao.cursor()
    
    
app=QtWidgets.QApplication([])
cadastros=uic.loadUi('cadastros.ui')
cadastros.btnSalvar.clicked.connect(inserir_dados)
cadastros.btnAnalise.clicked.connect(analise)
cadastros.btnRelatorio.clicked.connect(relatorio)

relatorio=uic.loadUi('relatorio.ui')
relatorio.btnEditar.clicked.connect(editar_dados)

editar=uic.loadUi('editar.ui')
    
cadastros.show()
app.exec()