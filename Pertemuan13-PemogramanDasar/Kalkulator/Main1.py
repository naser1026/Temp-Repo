import sys
from PyQt5.QtWidgets import QApplication
from CalcForm import *

if __name__ == '__main__' :
    a = QApplication(sys.argv)
    
    form = CalcForm()
    form.show()
    
    a.exec_()