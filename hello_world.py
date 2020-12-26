from PyQt5 import QtWidgets


app = QtWidgets.QApplication([])
window = QtWidgets.QWidget(windowTitle='Hello QT')
print(window.windowTitle())
window.show()
app.exec()

