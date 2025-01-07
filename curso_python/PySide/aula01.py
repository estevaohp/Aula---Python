import sys

from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

app = QApplication(sys.argv)

botao = QPushbutton('Texto do botão') # type: ignore
botao.setStyleSheet('font-size: 40px;')
botao.show()

central_widget = QWidget()

layout = QVBoxLayout()
layout.addWidget(botao)

layout.addWidget(botao, 1, 1)

central_widget.show()
app.exec()

