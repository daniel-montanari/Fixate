# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/dev/fixate_git/src/fixate/ui_gui_qt/fixateGUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FixateUI(object):
    def setupUi(self, FixateUI):
        FixateUI.setObjectName("FixateUI")
        FixateUI.setEnabled(True)
        FixateUI.resize(1200, 850)
        FixateUI.setBaseSize(QtCore.QSize(1200, 850))
        FixateUI.setFocusPolicy(QtCore.Qt.StrongFocus)
        FixateUI.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        FixateUI.setWindowTitle("Fixate")
        FixateUI.setWindowOpacity(1.0)
        FixateUI.setToolTip("")
        FixateUI.setStatusTip("Fixate")
        FixateUI.setWhatsThis("Fixate")
        FixateUI.setAccessibleName("Fixate")
        FixateUI.setAccessibleDescription("")
        FixateUI.setAutoFillBackground(False)
        FixateUI.setWindowFilePath("")
        FixateUI.setInputMethodHints(QtCore.Qt.ImhNone)
        FixateUI.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.MainWindow = QtWidgets.QWidget(FixateUI)
        self.MainWindow.setToolTip("")
        self.MainWindow.setStatusTip("")
        self.MainWindow.setWhatsThis("")
        self.MainWindow.setAccessibleName("")
        self.MainWindow.setAccessibleDescription("")
        self.MainWindow.setObjectName("MainWindow")
        self.gridLayout = QtWidgets.QGridLayout(self.MainWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.FrameLayout = QtWidgets.QVBoxLayout()
        self.FrameLayout.setContentsMargins(-1, -1, 0, 0)
        self.FrameLayout.setObjectName("FrameLayout")
        self.PaneLayout = QtWidgets.QHBoxLayout()
        self.PaneLayout.setContentsMargins(0, -1, 0, -1)
        self.PaneLayout.setObjectName("PaneLayout")
        self.TestTreeLayout = QtWidgets.QVBoxLayout()
        self.TestTreeLayout.setContentsMargins(-1, -1, 0, -1)
        self.TestTreeLayout.setObjectName("TestTreeLayout")
        self.TestTree = QtWidgets.QTreeWidget(self.MainWindow)
        self.TestTree.setEnabled(True)
        self.TestTree.setToolTip("")
        self.TestTree.setStatusTip("")
        self.TestTree.setWhatsThis("")
        self.TestTree.setAccessibleName("")
        self.TestTree.setAccessibleDescription("")
        self.TestTree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TestTree.setTabKeyNavigation(True)
        self.TestTree.setProperty("showDropIndicator", False)
        self.TestTree.setIndentation(10)
        self.TestTree.setRootIsDecorated(True)
        self.TestTree.setUniformRowHeights(True)
        self.TestTree.setAnimated(True)
        self.TestTree.setAllColumnsShowFocus(False)
        self.TestTree.setWordWrap(False)
        self.TestTree.setHeaderHidden(False)
        self.TestTree.setColumnCount(2)
        self.TestTree.setObjectName("TestTree")
        self.TestTree.headerItem().setText(0, "Name")
        self.TestTree.headerItem().setText(1, "Status")
        self.TestTree.headerItem().setTextAlignment(1, QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TestTree.header().setVisible(True)
        self.TestTree.header().setCascadingSectionResizes(False)
        self.TestTree.header().setDefaultSectionSize(120)
        self.TestTree.header().setHighlightSections(False)
        self.TestTree.header().setMinimumSectionSize(20)
        self.TestTree.header().setSortIndicatorShown(False)
        self.TestTree.header().setStretchLastSection(False)
        self.TestTreeLayout.addWidget(self.TestTree)
        self.PaneLayout.addLayout(self.TestTreeLayout)
        self.MainLayout = QtWidgets.QVBoxLayout()
        self.MainLayout.setContentsMargins(-1, -1, 0, -1)
        self.MainLayout.setObjectName("MainLayout")
        self.TitleLayout = QtWidgets.QHBoxLayout()
        self.TitleLayout.setContentsMargins(-1, 0, -1, -1)
        self.TitleLayout.setSpacing(2)
        self.TitleLayout.setObjectName("TitleLayout")
        self.InfoLayout = QtWidgets.QVBoxLayout()
        self.InfoLayout.setContentsMargins(-1, -1, 0, -1)
        self.InfoLayout.setObjectName("InfoLayout")
        self.ActiveTest = QtWidgets.QLabel(self.MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ActiveTest.sizePolicy().hasHeightForWidth())
        self.ActiveTest.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.ActiveTest.setFont(font)
        self.ActiveTest.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ActiveTest.setToolTip("")
        self.ActiveTest.setStatusTip("")
        self.ActiveTest.setWhatsThis("")
        self.ActiveTest.setAccessibleName("")
        self.ActiveTest.setAccessibleDescription("")
        self.ActiveTest.setText("")
        self.ActiveTest.setScaledContents(False)
        self.ActiveTest.setAlignment(QtCore.Qt.AlignCenter)
        self.ActiveTest.setWordWrap(False)
        self.ActiveTest.setIndent(10)
        self.ActiveTest.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.ActiveTest.setObjectName("ActiveTest")
        self.InfoLayout.addWidget(self.ActiveTest)
        self.TestDescription = QtWidgets.QLabel(self.MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TestDescription.sizePolicy().hasHeightForWidth())
        self.TestDescription.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.TestDescription.setFont(font)
        self.TestDescription.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.TestDescription.setToolTip("")
        self.TestDescription.setStatusTip("")
        self.TestDescription.setWhatsThis("")
        self.TestDescription.setAccessibleName("")
        self.TestDescription.setAccessibleDescription("")
        self.TestDescription.setText("")
        self.TestDescription.setScaledContents(False)
        self.TestDescription.setAlignment(QtCore.Qt.AlignCenter)
        self.TestDescription.setWordWrap(False)
        self.TestDescription.setIndent(10)
        self.TestDescription.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.TestDescription.setObjectName("TestDescription")
        self.InfoLayout.addWidget(self.TestDescription)
        self.InfoLayout.setStretch(0, 1)
        self.InfoLayout.setStretch(1, 1)
        self.TitleLayout.addLayout(self.InfoLayout)
        self.IndicatorContainer = QtWidgets.QWidget(self.MainWindow)
        self.IndicatorContainer.setObjectName("IndicatorContainer")
        self.IndicatorLayout = QtWidgets.QGridLayout(self.IndicatorContainer)
        self.IndicatorLayout.setContentsMargins(0, 0, 0, 0)
        self.IndicatorLayout.setObjectName("IndicatorLayout")
        self.WorkingIndicator = QtWidgets.QLabel(self.IndicatorContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WorkingIndicator.sizePolicy().hasHeightForWidth())
        self.WorkingIndicator.setSizePolicy(sizePolicy)
        self.WorkingIndicator.setToolTip("")
        self.WorkingIndicator.setStatusTip("")
        self.WorkingIndicator.setWhatsThis("")
        self.WorkingIndicator.setAccessibleName("")
        self.WorkingIndicator.setAccessibleDescription("")
        self.WorkingIndicator.setText("")
        self.WorkingIndicator.setObjectName("WorkingIndicator")
        self.IndicatorLayout.addWidget(self.WorkingIndicator, 0, 0, 1, 1)
        self.TitleLayout.addWidget(self.IndicatorContainer)
        self.TitleLayout.setStretch(0, 10)
        self.TitleLayout.setStretch(1, 1)
        self.MainLayout.addLayout(self.TitleLayout)
        self.ImageView = ResizeImageView(self.MainWindow)
        self.ImageView.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImageView.sizePolicy().hasHeightForWidth())
        self.ImageView.setSizePolicy(sizePolicy)
        self.ImageView.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ImageView.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ImageView.setAcceptDrops(False)
        self.ImageView.setToolTip("")
        self.ImageView.setStatusTip("")
        self.ImageView.setWhatsThis("")
        self.ImageView.setAccessibleName("")
        self.ImageView.setAutoFillBackground(True)
        self.ImageView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ImageView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ImageView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.ImageView.setInteractive(False)
        self.ImageView.setObjectName("ImageView")
        self.MainLayout.addWidget(self.ImageView)
        self.ButtonLayout = QtWidgets.QHBoxLayout()
        self.ButtonLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.ButtonLayout.setContentsMargins(50, -1, 50, -1)
        self.ButtonLayout.setSpacing(100)
        self.ButtonLayout.setObjectName("ButtonLayout")
        self.Button_1 = QtWidgets.QPushButton(self.MainWindow)
        self.Button_1.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_1.sizePolicy().hasHeightForWidth())
        self.Button_1.setSizePolicy(sizePolicy)
        self.Button_1.setText("")
        self.Button_1.setCheckable(False)
        self.Button_1.setDefault(False)
        self.Button_1.setFlat(False)
        self.Button_1.setObjectName("Button_1")
        self.ButtonLayout.addWidget(self.Button_1)
        self.Button_2 = QtWidgets.QPushButton(self.MainWindow)
        self.Button_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_2.sizePolicy().hasHeightForWidth())
        self.Button_2.setSizePolicy(sizePolicy)
        self.Button_2.setText("")
        self.Button_2.setObjectName("Button_2")
        self.ButtonLayout.addWidget(self.Button_2)
        self.Button_3 = QtWidgets.QPushButton(self.MainWindow)
        self.Button_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_3.sizePolicy().hasHeightForWidth())
        self.Button_3.setSizePolicy(sizePolicy)
        self.Button_3.setText("")
        self.Button_3.setObjectName("Button_3")
        self.ButtonLayout.addWidget(self.Button_3)
        self.ButtonLayout.setStretch(0, 1)
        self.ButtonLayout.setStretch(1, 1)
        self.ButtonLayout.setStretch(2, 1)
        self.MainLayout.addLayout(self.ButtonLayout)
        self.EventTabs = QtWidgets.QTabWidget(self.MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EventTabs.sizePolicy().hasHeightForWidth())
        self.EventTabs.setSizePolicy(sizePolicy)
        self.EventTabs.setToolTip("")
        self.EventTabs.setStatusTip("")
        self.EventTabs.setWhatsThis("")
        self.EventTabs.setAccessibleName("")
        self.EventTabs.setAccessibleDescription("")
        self.EventTabs.setObjectName("EventTabs")
        self.Active = QtWidgets.QWidget()
        self.Active.setToolTip("")
        self.Active.setStatusTip("")
        self.Active.setWhatsThis("")
        self.Active.setAccessibleName("")
        self.Active.setAccessibleDescription("")
        self.Active.setObjectName("Active")
        self.ActiveLayout = QtWidgets.QGridLayout(self.Active)
        self.ActiveLayout.setContentsMargins(1, 1, 1, 1)
        self.ActiveLayout.setVerticalSpacing(2)
        self.ActiveLayout.setObjectName("ActiveLayout")
        self.ActiveEvent = QtWidgets.QTextEdit(self.Active)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ActiveEvent.sizePolicy().hasHeightForWidth())
        self.ActiveEvent.setSizePolicy(sizePolicy)
        self.ActiveEvent.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.ActiveEvent.setFont(font)
        self.ActiveEvent.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.ActiveEvent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ActiveEvent.setToolTip("")
        self.ActiveEvent.setStatusTip("")
        self.ActiveEvent.setWhatsThis("")
        self.ActiveEvent.setAccessibleName("")
        self.ActiveEvent.setAccessibleDescription("")
        self.ActiveEvent.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ActiveEvent.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ActiveEvent.setLineWidth(1)
        self.ActiveEvent.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ActiveEvent.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ActiveEvent.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.ActiveEvent.setDocumentTitle("")
        self.ActiveEvent.setUndoRedoEnabled(False)
        self.ActiveEvent.setReadOnly(True)
        self.ActiveEvent.setAcceptRichText(False)
        self.ActiveEvent.setCursorWidth(1)
        self.ActiveEvent.setPlaceholderText("")
        self.ActiveEvent.setObjectName("ActiveEvent")
        self.ActiveLayout.addWidget(self.ActiveEvent, 0, 0, 1, 1)
        self.UserInputBox = SubmissionTextBox(self.Active)
        self.UserInputBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UserInputBox.sizePolicy().hasHeightForWidth())
        self.UserInputBox.setSizePolicy(sizePolicy)
        self.UserInputBox.setMinimumSize(QtCore.QSize(0, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 202, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 202, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.UserInputBox.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.UserInputBox.setFont(font)
        self.UserInputBox.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.UserInputBox.setAcceptDrops(False)
        self.UserInputBox.setToolTip("")
        self.UserInputBox.setStatusTip("")
        self.UserInputBox.setWhatsThis("")
        self.UserInputBox.setAccessibleName("")
        self.UserInputBox.setAccessibleDescription("")
        self.UserInputBox.setDocumentTitle("")
        self.UserInputBox.setUndoRedoEnabled(False)
        self.UserInputBox.setReadOnly(False)
        self.UserInputBox.setPlainText("")
        self.UserInputBox.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.UserInputBox.setMaximumBlockCount(1)
        self.UserInputBox.setPlaceholderText("")
        self.UserInputBox.setObjectName("UserInputBox")
        self.ActiveLayout.addWidget(self.UserInputBox, 1, 0, 1, 1)
        self.ActiveLayout.setRowStretch(0, 7)
        self.ActiveLayout.setRowStretch(1, 1)
        self.EventTabs.addTab(self.Active, "")
        self.History = QtWidgets.QWidget()
        self.History.setToolTip("")
        self.History.setStatusTip("")
        self.History.setWhatsThis("")
        self.History.setAccessibleName("")
        self.History.setAccessibleDescription("")
        self.History.setObjectName("History")
        self.HistoryLayout = QtWidgets.QGridLayout(self.History)
        self.HistoryLayout.setContentsMargins(1, 1, 1, 1)
        self.HistoryLayout.setObjectName("HistoryLayout")
        self.Events = QtWidgets.QTextEdit(self.History)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Events.sizePolicy().hasHeightForWidth())
        self.Events.setSizePolicy(sizePolicy)
        self.Events.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.Events.setFont(font)
        self.Events.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Events.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Events.setToolTip("")
        self.Events.setStatusTip("")
        self.Events.setWhatsThis("")
        self.Events.setAccessibleName("")
        self.Events.setAccessibleDescription("")
        self.Events.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Events.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Events.setLineWidth(1)
        self.Events.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Events.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Events.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.Events.setDocumentTitle("")
        self.Events.setUndoRedoEnabled(False)
        self.Events.setReadOnly(True)
        self.Events.setAcceptRichText(False)
        self.Events.setCursorWidth(1)
        self.Events.setObjectName("Events")
        self.HistoryLayout.addWidget(self.Events, 0, 0, 1, 1)
        self.EventTabs.addTab(self.History, "")
        self.ErrorLog = QtWidgets.QWidget()
        self.ErrorLog.setToolTip("")
        self.ErrorLog.setStatusTip("")
        self.ErrorLog.setWhatsThis("")
        self.ErrorLog.setAccessibleName("")
        self.ErrorLog.setAccessibleDescription("")
        self.ErrorLog.setObjectName("ErrorLog")
        self.ErrorLayout = QtWidgets.QGridLayout(self.ErrorLog)
        self.ErrorLayout.setContentsMargins(1, 1, 1, 1)
        self.ErrorLayout.setObjectName("ErrorLayout")
        self.Errors = QtWidgets.QTextEdit(self.ErrorLog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Errors.sizePolicy().hasHeightForWidth())
        self.Errors.setSizePolicy(sizePolicy)
        self.Errors.setMinimumSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.Errors.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Errors.setFont(font)
        self.Errors.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Errors.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Errors.setToolTip("")
        self.Errors.setStatusTip("")
        self.Errors.setWhatsThis("")
        self.Errors.setAccessibleName("")
        self.Errors.setAccessibleDescription("")
        self.Errors.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Errors.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Errors.setLineWidth(1)
        self.Errors.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Errors.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Errors.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.Errors.setDocumentTitle("")
        self.Errors.setUndoRedoEnabled(False)
        self.Errors.setReadOnly(True)
        self.Errors.setAcceptRichText(False)
        self.Errors.setCursorWidth(1)
        self.Errors.setObjectName("Errors")
        self.ErrorLayout.addWidget(self.Errors, 0, 0, 1, 1)
        self.EventTabs.addTab(self.ErrorLog, "")
        self.MainLayout.addWidget(self.EventTabs)
        self.MainLayout.setStretch(0, 3)
        self.MainLayout.setStretch(1, 12)
        self.MainLayout.setStretch(2, 2)
        self.MainLayout.setStretch(3, 7)
        self.PaneLayout.addLayout(self.MainLayout)
        self.PaneLayout.setStretch(0, 1)
        self.PaneLayout.setStretch(1, 3)
        self.FrameLayout.addLayout(self.PaneLayout)
        self.ProgressBar = QtWidgets.QProgressBar(self.MainWindow)
        self.ProgressBar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ProgressBar.setToolTip("")
        self.ProgressBar.setStatusTip("")
        self.ProgressBar.setWhatsThis("")
        self.ProgressBar.setAccessibleName("")
        self.ProgressBar.setAccessibleDescription("")
        self.ProgressBar.setAutoFillBackground(False)
        self.ProgressBar.setStyleSheet("QProgressBar{\n"
"    padding: 1px;\n"
"    margin-right: 32px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #baf3bc, stop: 0.6 #05d431);\n"
"    margin: 0px;\n"
"    width: 1px;\n"
"}")
        self.ProgressBar.setProperty("value", 0)
        self.ProgressBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ProgressBar.setTextVisible(True)
        self.ProgressBar.setObjectName("ProgressBar")
        self.FrameLayout.addWidget(self.ProgressBar)
        self.gridLayout.addLayout(self.FrameLayout, 0, 1, 1, 1)
        FixateUI.setCentralWidget(self.MainWindow)

        self.retranslateUi(FixateUI)
        self.EventTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FixateUI)

    def retranslateUi(self, FixateUI):
        _translate = QtCore.QCoreApplication.translate
        self.EventTabs.setTabText(self.EventTabs.indexOf(self.Active), _translate("FixateUI", "Active"))
        self.EventTabs.setTabText(self.EventTabs.indexOf(self.History), _translate("FixateUI", "History"))
        self.EventTabs.setTabText(self.EventTabs.indexOf(self.ErrorLog), _translate("FixateUI", "Errors"))

from fixate.ui_gui_qt.subclassed_widgets import ResizeImageView, SubmissionTextBox
