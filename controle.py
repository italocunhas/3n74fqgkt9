from PyQt5 import uic, QtWidgets


app=QtWidgets.QApplication([])
cadastros=uic.loadUi('cadastros.ui')

cadastros.show()
app.exec()