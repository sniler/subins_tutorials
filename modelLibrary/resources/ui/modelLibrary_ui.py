# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/subins_tutorials/modelLibrary/resources/ui/modelLibrary_ui.ui'
#
# Created: Fri Jan 18 22:48:04 2019
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(960, 597)
        MainWindow.setStyleSheet(_fromUtf8("font: 12pt \"MS Shell Dlg 2\";"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.scrollArea_pose = QtGui.QScrollArea(self.splitter)
        self.scrollArea_pose.setStyleSheet(_fromUtf8("font: 10pt \"MS Shell Dlg 2\";"))
        self.scrollArea_pose.setWidgetResizable(True)
        self.scrollArea_pose.setObjectName(_fromUtf8("scrollArea_pose"))
        self.scrollAreaWidget_pose = QtGui.QWidget()
        self.scrollAreaWidget_pose.setGeometry(QtCore.QRect(0, 0, 305, 558))
        self.scrollAreaWidget_pose.setObjectName(_fromUtf8("scrollAreaWidget_pose"))
        self.gridLayout_poseList = QtGui.QGridLayout(self.scrollAreaWidget_pose)
        self.gridLayout_poseList.setMargin(1)
        self.gridLayout_poseList.setSpacing(1)
        self.gridLayout_poseList.setObjectName(_fromUtf8("gridLayout_poseList"))
        self.treeWidget = QtGui.QTreeWidget(self.scrollAreaWidget_pose)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.treeWidget.header().setVisible(False)
        self.gridLayout_poseList.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.scrollArea_pose.setWidget(self.scrollAreaWidget_pose)
        self.groupBox_pose = QtGui.QGroupBox(self.splitter)
        self.groupBox_pose.setObjectName(_fromUtf8("groupBox_pose"))
        self.verticalLayout_pose = QtGui.QVBoxLayout(self.groupBox_pose)
        self.verticalLayout_pose.setSpacing(10)
        self.verticalLayout_pose.setMargin(10)
        self.verticalLayout_pose.setObjectName(_fromUtf8("verticalLayout_pose"))
        self.groupBox_snapShot = QtGui.QGroupBox(self.groupBox_pose)
        self.groupBox_snapShot.setObjectName(_fromUtf8("groupBox_snapShot"))
        self.horizontalLayout_snapShot = QtGui.QHBoxLayout(self.groupBox_snapShot)
        self.horizontalLayout_snapShot.setSpacing(5)
        self.horizontalLayout_snapShot.setMargin(5)
        self.horizontalLayout_snapShot.setObjectName(_fromUtf8("horizontalLayout_snapShot"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_snapShot.addItem(spacerItem)
        self.button_snapShot = QtGui.QPushButton(self.groupBox_snapShot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_snapShot.sizePolicy().hasHeightForWidth())
        self.button_snapShot.setSizePolicy(sizePolicy)
        self.button_snapShot.setMinimumSize(QtCore.QSize(150, 150))
        self.button_snapShot.setMaximumSize(QtCore.QSize(150, 150))
        self.button_snapShot.setText(_fromUtf8(""))
        self.button_snapShot.setObjectName(_fromUtf8("button_snapShot"))
        self.horizontalLayout_snapShot.addWidget(self.button_snapShot)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_snapShot.addItem(spacerItem1)
        self.verticalLayout_pose.addWidget(self.groupBox_snapShot)
        self.groupBox_poseLabel = QtGui.QGroupBox(self.groupBox_pose)
        self.groupBox_poseLabel.setObjectName(_fromUtf8("groupBox_poseLabel"))
        self.horizontalLayout_poseLabel = QtGui.QHBoxLayout(self.groupBox_poseLabel)
        self.horizontalLayout_poseLabel.setSpacing(5)
        self.horizontalLayout_poseLabel.setMargin(5)
        self.horizontalLayout_poseLabel.setObjectName(_fromUtf8("horizontalLayout_poseLabel"))
        self.label_poseLabel = QtGui.QLabel(self.groupBox_poseLabel)
        self.label_poseLabel.setObjectName(_fromUtf8("label_poseLabel"))
        self.horizontalLayout_poseLabel.addWidget(self.label_poseLabel)
        self.lineEdit_poseLabel = QtGui.QLineEdit(self.groupBox_poseLabel)
        self.lineEdit_poseLabel.setText(_fromUtf8(""))
        self.lineEdit_poseLabel.setObjectName(_fromUtf8("lineEdit_poseLabel"))
        self.horizontalLayout_poseLabel.addWidget(self.lineEdit_poseLabel)
        self.verticalLayout_pose.addWidget(self.groupBox_poseLabel)
        self.textEdit_history = QtGui.QTextEdit(self.groupBox_pose)
        self.textEdit_history.setStyleSheet(_fromUtf8(""))
        self.textEdit_history.setReadOnly(True)
        self.textEdit_history.setObjectName(_fromUtf8("textEdit_history"))
        self.verticalLayout_pose.addWidget(self.textEdit_history)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_pose.addItem(spacerItem2)
        self.groupBox_blend = QtGui.QGroupBox(self.groupBox_pose)
        self.groupBox_blend.setObjectName(_fromUtf8("groupBox_blend"))
        self.horizontalLayout_blend = QtGui.QHBoxLayout(self.groupBox_blend)
        self.horizontalLayout_blend.setSpacing(5)
        self.horizontalLayout_blend.setMargin(5)
        self.horizontalLayout_blend.setObjectName(_fromUtf8("horizontalLayout_blend"))
        self.slider_poseBlend = QtGui.QSlider(self.groupBox_blend)
        self.slider_poseBlend.setMinimum(-100)
        self.slider_poseBlend.setMaximum(200)
        self.slider_poseBlend.setProperty("value", 100)
        self.slider_poseBlend.setOrientation(QtCore.Qt.Horizontal)
        self.slider_poseBlend.setObjectName(_fromUtf8("slider_poseBlend"))
        self.horizontalLayout_blend.addWidget(self.slider_poseBlend)
        self.button_blendValue = QtGui.QPushButton(self.groupBox_blend)
        self.button_blendValue.setMinimumSize(QtCore.QSize(50, 20))
        self.button_blendValue.setMaximumSize(QtCore.QSize(50, 20))
        self.button_blendValue.setStyleSheet(_fromUtf8("font: 10pt \"MS Shell Dlg 2\";"))
        self.button_blendValue.setObjectName(_fromUtf8("button_blendValue"))
        self.horizontalLayout_blend.addWidget(self.button_blendValue)
        self.verticalLayout_pose.addWidget(self.groupBox_blend)
        self.button_save = QtGui.QPushButton(self.groupBox_pose)
        self.button_save.setObjectName(_fromUtf8("button_save"))
        self.verticalLayout_pose.addWidget(self.button_save)
        self.listWidget = QtGui.QListWidget(self.splitter)
        self.listWidget.setAutoScrollMargin(36)
        self.listWidget.setTabKeyNavigation(True)
        self.listWidget.setDragEnabled(True)
        self.listWidget.setDragDropOverwriteMode(True)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setIconSize(QtCore.QSize(600, 600))
        self.listWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.listWidget.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.listWidget.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.listWidget.setMovement(QtGui.QListView.Snap)
        self.listWidget.setFlow(QtGui.QListView.LeftToRight)
        self.listWidget.setProperty("isWrapping", True)
        self.listWidget.setResizeMode(QtGui.QListView.Adjust)
        self.listWidget.setLayoutMode(QtGui.QListView.Batched)
        self.listWidget.setSpacing(10)
        self.listWidget.setViewMode(QtGui.QListView.IconMode)
        self.listWidget.setModelColumn(0)
        self.listWidget.setUniformItemSizes(True)
        self.listWidget.setBatchSize(500)
        self.listWidget.setWordWrap(True)
        self.listWidget.setSelectionRectVisible(True)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menu_bar = QtGui.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 960, 25))
        self.menu_bar.setObjectName(_fromUtf8("menu_bar"))
        self.menu_file = QtGui.QMenu(self.menu_bar)
        self.menu_file.setObjectName(_fromUtf8("menu_file"))
        self.menu_settings = QtGui.QMenu(self.menu_bar)
        self.menu_settings.setObjectName(_fromUtf8("menu_settings"))
        self.menu_help = QtGui.QMenu(self.menu_bar)
        self.menu_help.setObjectName(_fromUtf8("menu_help"))
        MainWindow.setMenuBar(self.menu_bar)
        self.action_create = QtGui.QAction(MainWindow)
        self.action_create.setObjectName(_fromUtf8("action_create"))
        self.action_remove = QtGui.QAction(MainWindow)
        self.action_remove.setObjectName(_fromUtf8("action_remove"))
        self.action_quit = QtGui.QAction(MainWindow)
        self.action_quit.setObjectName(_fromUtf8("action_quit"))
        self.action_preferences = QtGui.QAction(MainWindow)
        self.action_preferences.setObjectName(_fromUtf8("action_preferences"))
        self.action_aboutools = QtGui.QAction(MainWindow)
        self.action_aboutools.setObjectName(_fromUtf8("action_aboutools"))
        self.action_abouttoolkits = QtGui.QAction(MainWindow)
        self.action_abouttoolkits.setObjectName(_fromUtf8("action_abouttoolkits"))
        self.menu_file.addAction(self.action_create)
        self.menu_file.addAction(self.action_remove)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_quit)
        self.menu_settings.addAction(self.action_preferences)
        self.menu_help.addAction(self.action_aboutools)
        self.menu_help.addAction(self.action_abouttoolkits)
        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menu_settings.menuAction())
        self.menu_bar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_pose.setTitle(_translate("MainWindow", "Pose", None))
        self.label_poseLabel.setText(_translate("MainWindow", "Name", None))
        self.textEdit_history.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#aaaa00;\">&quot;My Pose Library v0.1&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#aaaa00;\">Data    : April 11, 2017</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#aaaa00;\">last modified  : April 15, 2017</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#aaaa00;\">Author    : Subin Gopi</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#aaaa00;\">subing85@gmail.com</span></p></body></html>", None))
        self.button_blendValue.setText(_translate("MainWindow", "100", None))
        self.button_save.setText(_translate("MainWindow", "Save", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "New Item", None))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "New Item", None))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "New Item", None))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "New Item", None))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "New Item", None))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "New Item", None))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "New Item", None))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "New Item", None))
        item = self.listWidget.item(8)
        item.setText(_translate("MainWindow", "New Item", None))
        item = self.listWidget.item(9)
        item.setText(_translate("MainWindow", "New Item", None))
        item = self.listWidget.item(10)
        item.setText(_translate("MainWindow", "New Item", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.menu_file.setTitle(_translate("MainWindow", "File", None))
        self.menu_settings.setTitle(_translate("MainWindow", "Settings", None))
        self.menu_help.setTitle(_translate("MainWindow", "Help", None))
        self.action_create.setText(_translate("MainWindow", "Create Folder", None))
        self.action_remove.setText(_translate("MainWindow", "Remove Folder", None))
        self.action_quit.setText(_translate("MainWindow", "Quit", None))
        self.action_preferences.setText(_translate("MainWindow", "Preferences", None))
        self.action_aboutools.setText(_translate("MainWindow", "About Tools", None))
        self.action_abouttoolkits.setText(_translate("MainWindow", "About Subi\'s Tool Kits", None))

import aa_rc
