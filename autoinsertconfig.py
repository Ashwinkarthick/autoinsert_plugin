"""
config
Created by Jonathan deWerd on 2012-01-19.
"""
import util, cadnano
from . import autoinsertconfig_ui
from . import autoinsert
util.qtWrapImport('QtGui', globals(), ['QKeySequence'])
util.qtWrapImport('QtCore', globals(), ['Qt'])
util.qtWrapImport('QtWidgets', globals(), ['QDialog', 'QDialogButtonBox'])


class AutoinsertConfig(QDialog, autoinsertconfig_ui.Ui_Dialog):
    def __init__(self, parent, handler):
        QDialog.__init__(self, parent, Qt.Sheet)
        self.setupUi(self)
        self.handler = handler
        fb = self.buttonBox.button(QDialogButtonBox.Cancel)
        fb.setShortcut(QKeySequence(Qt.CTRL | Qt.Key_R ))

    def keyPressEvent(self, e):
        return QDialog.keyPressEvent(self, e)

    def closeDialog(self):
        self.close()

    def accept(self):
        part = self.handler.doc.controller().activePart()
        if part != None:
            settings = {\
                'targetBpbetweenInsertions'             : self.targetBpbetweenInsertionsBox.value(),\
                'initialPosition'          				: self.initialPositionBox.value(),\
                'numOfInsertions'					    : self.numOfInsertionsBox.value(),\
                'numberofHelices'    					: '2',\
            }
            self.handler.win.pathGraphicsView.setViewportUpdateOn(False)
            # print "pre verify"
            # part.verifyOligos()
            # print "insertStaples"
            autoinsert.insertExtraBp(part, settings)
            # print "post break verify"
            # part.verifyOligos()
            self.handler.win.pathGraphicsView.setViewportUpdateOn(True)
        self.close()
