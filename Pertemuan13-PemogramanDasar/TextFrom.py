from PyQt5.QtWidgets import QWidget,QLabel

class TextForm(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setupUI()
        
    def setupUI(self) :
        self.resize(300, 200)
        self.move(300, 300)
        self.setWindowTitle("Demo Tag HTML")
        
        self.label1 = QLabel(
            '<h1>Hello<font color = red> World!</font></h1>'
        )
        self.label1.move(10, 10)
        self.setParent(self)
        
        self.label2 = QLabel('''
            Contoh text <b>Cetak Tebal</b> <i>Cetak Miring</i> dan <u>Garis Bawah</u>'''
        )
        self.label2.wordWrap(True)
        self.label2.move(10, 20)
        self.label2.setParent(self)
        