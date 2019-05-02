# to run make sure you are in the right directory and type test.py you should now have a window.
# imports the application, the layout, the controls like buttons, and the widgets.      
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,QLabel

# inicializes the application, you only need 1 per app.
app = QApplication([])
# makes a window for the application.
window = QWidget()
# tells python we want to use the Vbox layout for our controls.
layout = QVBoxLayout()
# adds a button. 
layout.addWidget(QPushButton('this button should be accessible'))
# adds a label. 
layout.addWidget(QLabel('this is a label and i read correctly hello world!'))
# sets the window layout.
window.setLayout(layout)
# shows the window on screen.
window.show()
# closes the app.
app.exec_()

