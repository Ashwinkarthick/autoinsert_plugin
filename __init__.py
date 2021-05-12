from .autoinsertconfig import AutoinsertConfig
import cadnano, util
util.qtWrapImport('QtGui', globals(), ['QIcon', 'QPixmap'])
util.qtWrapImport('QtWidgets', globals(), ['QAction'])


class ExtraBpHandler(object):
	def __init__(self, document, window):
		self.doc, self.win = document, window
		icon10 = QIcon()
		icon10.addPixmap(QPixmap(":/pathtools/insert"), QIcon.Normal, QIcon.Off)
		self.actionExtraBp = QAction(window)
		self.actionExtraBp.setIcon(icon10)
		self.actionExtraBp.setText('AutoInsert')
		self.actionExtraBp.setToolTip("Click this button to generate a default set of staples.")
		self.actionExtraBp.setObjectName("actionExtraBp")
		self.actionExtraBp.triggered.connect(self.actionExtraBpSlot)
		self.win.menuPlugins.addAction(self.actionExtraBp)
		self.win.topToolBar.insertAction(self.win.actionFiltersLabel, self.actionExtraBp)
		self.win.topToolBar.insertSeparator(self.win.actionFiltersLabel)
		self.configDialog = None

	def actionExtraBpSlot(self):
		"""Only show the dialog if staple strands exist."""
		part = self.doc.controller().activePart()
		if part != None:  # is there a part?
			for vh in part.getVirtualHelices():
				scafSS = vh.scaffoldStrandSet()
				for o in list(part.oligos()):
					if o.isStaple():  # is there a staple oligo?
						if self.configDialog == None:
							self.configDialog = AutoinsertConfig(self.win, self)
						self.configDialog.show()
						return


def documentWindowWasCreatedSlot(doc, win):
	doc.extraBpHandler = ExtraBpHandler(doc, win)

# Initialization
for c in cadnano.app().documentControllers:
	doc, win = c.document(), c.window()
	doc.extraBpHandler = ExtraBpHandler(doc, win)
cadnano.app().documentWindowWasCreatedSignal.connect(documentWindowWasCreatedSlot)
