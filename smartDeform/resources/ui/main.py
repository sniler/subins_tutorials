'''
import shiboken
from maya import OpenMayaUI
from PySide import QtGui
from smartDeform.resources.ui import main
main_window = shiboken.wrapInstance(long(omu.MQtUtil.mainWindow()),QtGui.QWidget)
my_window = main.MainWindow(parent=main_window)
my_window.show()
'''


import os
import sys


path = '/venture/subins_tutorials'
if path not in sys.path:
    sys.path.append(path)
    
from PySide import QtGui
from PySide import QtCore
from functools import partial

from smartDeform.resources.ui import geometry
from smartDeform.resources.ui import mirror
from smartDeform.resources.ui import weights

reload(geometry)
reload(mirror)
reload(weights)


class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
                
        self.geometry = geometry.Geometry(parent=self)
        self.my_mirror = mirror.Mirror(parent=self)        
        self.weights = weights.Weights(parent=self)        
        self.setupUi()
        self.setParent(parent)
        
    
    def setParent(self, parent):
        #from pymel import core
        pass
        
        #if core.dockControl ('Mainwindow_subin', q=1, ex=1) :
        #    core.deleteUI('Mainwindow_subin', ctl=1)
        
        #floating_layout = core.paneLayout (cn='single', w=300, p=parent)        
        #core.dockControl ('Mainwindow_subin', l='Smart Deformer 0.0.1', area='right', content=floatingLayout, allowedArea=['right', 'left'])        
        #core.control ('Mainwindow_subin', e=1, p=floatingLayout)

    def setupUi(self):
        self.resize(500, 800)
        self.setObjectName('Mainwindow_subin')
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralwidget)

        self.verticallayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(0)
        self.verticallayout.setContentsMargins(10, 10, 10, 10)           

        self.toolbox = QtGui.QToolBox(self.centralwidget)
        self.toolbox.setObjectName('toolBox')
        self.verticallayout.addWidget(self.toolbox)

        self.page_convert = QtGui.QWidget()
        self.page_convert.setGeometry(QtCore.QRect(0, 0, 599, 314))
        self.page_convert.setObjectName('page_convert')
        self.toolbox.addItem(self.page_convert, 'Convert')

        self.verticallayout_convert = QtGui.QVBoxLayout(self.page_convert)
        self.verticallayout_convert.setObjectName('verticallayout_convert')
        #  self.verticallayout_convert.addWidget(self.from_button)
        # self.verticallayout_convert.addWidget(self.to_button)
        self.verticallayout_convert.setSpacing(5)
        self.verticallayout_convert.setContentsMargins(10, 0, 0, 0)   

        self.horizontallayout_convert = QtGui.QHBoxLayout()
        self.horizontallayout_convert.setObjectName('horizontallayout_convert')
        self.verticallayout_convert.addLayout(self.horizontallayout_convert)                
        self.horizontallayout_convert.setSpacing(0)
        self.horizontallayout_convert.setContentsMargins(0, 0, 0, 0)  
        self.horizontallayout_convert.addWidget(self.geometry)
                
        self.page_cluster = QtGui.QWidget()
        self.page_cluster.setGeometry(QtCore.QRect(0, 0, 599, 314))
        self.page_cluster.setObjectName('page_cluster')
        self.toolbox.addItem(self.page_cluster, 'Mirror and ...')

        self.verticallayout_cluster = QtGui.QVBoxLayout(self.page_cluster)
        self.verticallayout_cluster.setObjectName('verticalLayout_cluster')
        self.verticallayout_cluster.addWidget(self.my_mirror)
        # self.verticallayout_cluster.addWidget(self.my_cluster)
        self.verticallayout_cluster.setSpacing(0)
        self.verticallayout_cluster.setContentsMargins(10, 0, 0, 0)  
                
        spaceritem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticallayout_cluster.addItem(spaceritem)
        
        self.page_weights = QtGui.QWidget()
        self.page_weights.setGeometry(QtCore.QRect(0, 0, 599, 314))
        self.page_weights.setObjectName('page_cluster')
        self.toolbox.addItem(self.page_weights, 'Weights')

        self.verticallayout_weights = QtGui.QVBoxLayout(self.page_weights)
        self.verticallayout_weights.setObjectName('verticalLayout_weights')
        self.verticallayout_weights.addWidget(self.weights)
        self.verticallayout_weights.setSpacing(0)
        self.verticallayout_weights.setContentsMargins(10, 0, 0, 0)  
        
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 599, 314))
        self.page.setObjectName('page_cluster')
        self.toolbox.addItem(self.page, 'Credits')
        self.toolbox.setCurrentIndex(2)

        # add moduless
        
    def convert(self):
        print ''

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow(parent=None)
    window.show()
    sys.exit(app.exec_())
