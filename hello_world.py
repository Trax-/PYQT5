from PyQt5 import QtWidgets as qtw


app = qtw.QApplication([])
window = qtw.QWidget(windowTitle='Hello QT')
print(window.windowTitle())
window.show()
app.exec()

