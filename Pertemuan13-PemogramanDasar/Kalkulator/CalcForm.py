from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont

class CalcForm(QWidget):
    def __init__(self) :
        super().__init__()
        self.setupUI()
        
    def setupUI(self) :
        self.resize(450, 600)
        self.setWindowTitle("Kalkulator-Sederhana")
        font = QFont()
        font.setPointSize(40)
        
        # Layar
        self.screenlabel = QLineEdit()
        self.screenlabel.setFont(font)
        layout = QVBoxLayout()
        layout.addWidget(self.screenlabel)
        self.setLayout(layout)
        
        self.setStyleSheet('''background: qlineargradient(x1:0, y1:0, x2:1, y2:1,stop:0 #294334, stop:0.5 #3D9362, stop:1 #00FF6E)''')
        buttonGrid = QGridLayout()
        layout.addLayout(buttonGrid)
                
        buttons = [
            '**', ' ', '<', 'C',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
        ]
        positions = [(i, j) for i in range(5) for j in range(4)]

        # Membuat dan menambahkan tombol ke dalam grid layout
        for position, buttonLabel in zip(positions, buttons):
            button = QPushButton(buttonLabel)
            button.setFont(font)
            button.clicked.connect(self.buttonClick)
            buttonGrid.addWidget(button, *position)
        
    def buttonClick(self) :
        button = self.sender()
        buttonLabel = button.text()
        if buttonLabel == '=' :
            expression = self.screenlabel.text()
            try :
                result = eval(expression)
                self.screenlabel.setText(str(result))
            except :
                self.screenlabel.setText("error")
        
        elif buttonLabel == '<' :
            tempLabel = str(self.screenlabel.text())[:-1]
            self.screenlabel.setText(tempLabel)
        
        elif buttonLabel == 'C' :
            self.screenlabel.setText('')
        
        else :
            currentText = self.screenlabel.text()
            self.screenlabel.setText(currentText + buttonLabel)