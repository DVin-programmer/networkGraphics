from PyQt5 import Qt as qt
import sys

app = qt.QApplication(sys.argv)
mw = qt.QMainWindow()
fr = qt.QFrame()
lt = qt.QVBoxLayout()
te = qt.QTextEdit("Some text")
fr.setLayout(lt)
lt.addWidget(te)
mw.setCentralWidget(fr)

ac = qt.QAction(te)
ac.setShortcut(qt.QKeySequence("Ctrl+K"))
te.addAction(ac)


def on_action_triggered(checked):
    tc = te.textCursor()
    tc.movePosition(qt.QTextCursor.Left, qt.QTextCursor.MoveAnchor, 1)
    te.setTextCursor(tc)


ac.triggered.connect(on_action_triggered)

mw.show()
app.exec_()