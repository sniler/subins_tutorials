import os
import sys
import warnings

from pprint import pprint

path = '/venture/subins_tutorials'
if path not in sys.path:
    sys.path.append(path)

from PySide import QtGui
from PySide import QtCore
from functools import partial
from datetime import datetime

from maya import OpenMaya
from maya import OpenMayaAnim

from smartDeform import resources

from smartDeform.modules import cluster
from smartDeform.modules import skincluster
from smartDeform.modules import studioMaya
from smartDeform.modules import readWrite

reload(resources)
reload(studioMaya)
reload(cluster)
reload(skincluster)
reload(readWrite)


class Weights(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Weights, self).__init__(parent=None)
        self.setupUi()

        self.cluster = cluster.Cluster()
        self.skincluster = skincluster.Skincluster()
        self.my_maya = studioMaya.Maya()        

    def setupUi(self):
        self.setObjectName('mirror')
        self.resize(300, 400)
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(0)
        self.verticallayout.setContentsMargins(0, 0, 0, 0)

        self.groupbox = QtGui.QGroupBox(self)
        self.groupbox.setObjectName('groupbox')
        self.groupbox.setTitle('Cluster Mirror')
        self.verticallayout.addWidget(self.groupbox)

        self.verticallayout_weight = QtGui.QVBoxLayout(self.groupbox)
        self.verticallayout_weight.setObjectName('verticallayout_weight')
        self.verticallayout_weight.setSpacing(1)
        self.verticallayout_weight.setContentsMargins(1, 1, 1, 1)

        self.listwidget = QtGui.QListWidget(self.groupbox)
        self.listwidget.setObjectName('listwidget')
        self.listwidget.setSelectionMode(
            QtGui.QAbstractItemView.ExtendedSelection)
        self.listwidget.setAlternatingRowColors(True)
        self.verticallayout_weight.addWidget(self.listwidget)

        self.horizontallayout_weight = QtGui.QHBoxLayout()
        self.horizontallayout_weight.setObjectName('horizontallayout_weight')
        self.horizontallayout_weight.setSpacing(1)
        self.horizontallayout_weight.setContentsMargins(1, 1, 1, 1)
        self.verticallayout_weight.addLayout(self.horizontallayout_weight)

        self.button_export = QtGui.QPushButton(self.groupbox)
        self.button_export.setObjectName('button_export')
        self.button_export.setText('Export')
        self.horizontallayout_weight.addWidget(self.button_export)

        self.button_import = QtGui.QPushButton(self.groupbox)
        self.button_import.setObjectName('button_import')
        self.button_import.setText('Import')
        self.horizontallayout_weight.addWidget(self.button_import)

        self.button_export.clicked.connect(self.exports)
        self.button_import.clicked.connect(self.imports)
        
        self.load_weigtss()
        
        self.popMenu(self.listwidget)
        

    def popMenu (self, listwidget) :     
        #custom Context Menu        
        listwidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)        
        listwidget.customContextMenuRequested.connect(partial (self.contextMenu, listwidget))

        self.pop_menu    = QtGui.QMenu (self)
        
        self.action_lock = QtGui.QAction(self)
        self.action_lock.setText('Lock Weights')        
        self.pop_menu.addAction (self.action_lock)
        
        self.action_unlock = QtGui.QAction(self)
        self.action_unlock.setText('Unlock Weights')        
        self.pop_menu.addAction (self.action_unlock)
       
    #Right click menu
    def contextMenu (self, listwidget, point) :        
        index = listwidget.indexAt (point)
        if not index.isValid():
            return        
        
        if self.current_deformer!='skinCluster':
            return
                
        self.pop_menu.exec_ (QtGui.QCursor.pos())
        
    def load_weigtss(self):
        self.listwidget.clear()
        rw = readWrite.ReadWrite(t='weights')        
        self.bundles = rw.getBundles()        
        for each_bundle, bundle_data in self.bundles.items():            
            item = QtGui.QListWidgetItem()
            item.setText(each_bundle)            
            current_icon = os.path.join(resources.getIconPath(),
                                '{}.png'.format(bundle_data['tag']))
            icon = QtGui.QIcon ()
            icon.addPixmap(QtGui.QPixmap(current_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)           
            item.setIcon (icon)            
            item.setToolTip('\n'.join(bundle_data['data'].keys()))                       
            self.listwidget.addItem(item)


    def exports(self):
        selections = self.my_maya.getSelectedDagPaths()
        drivers = {}        

        for index in range(selections.length()):            
            if not selections[index].isValid():
                continue            
            tag = None
            if self.my_maya.hasJoint(selections[index]):
                tag = 'joint'        
            elif self.my_maya.hasCluster(selections[index]):
                tag = 'cluster'                            
            drivers.setdefault(tag, []).append(selections[index])
 
        if None in drivers:
            # raise ValueError('#Unwanted nodes are found in the selection')
            OpenMaya.MGlobal.displayError(
                '#Unwanted nodes are found in your selection')
            return
 
        if drivers.keys().count(drivers.keys()[0]) != len(drivers.keys()):
            OpenMaya.MGlobal.displayError(
                '#You selected differ types of nodes\nselect cluster handless either joints')
            return
        
        file_name, ok = QtGui.QInputDialog.getText(self, 'Folder Name',
                            'Enter the folder name:', QtGui.QLineEdit.Normal)
         
        if not ok:
            OpenMaya.MGlobal.displayWarning('#Abrot your export!...')
            return
        
        weights = {}        
        if drivers.keys()[0]=='cluster':             
            weights = self.cluster.get_weights(drivers['cluster'])           

        comment = 'smart tool 0.0.1 - weights container'
        created_date = datetime.now().strftime('%B/%d/%Y - %I:%M:%S:%p')
        description = 'This data contain information about maya 2016 deformers weights'
        type = 'weights'
        valid = True
        data = weights
        tag = drivers.keys()[0]
         
        rw = readWrite.ReadWrite(c=comment, cd=created_date,
                    d=description, t=type, v=valid, data=data, tag=tag)
        rw.create(name=str(file_name))
        print rw.file_path
        

    def imports(self):        
        if not self.bundles:
            OpenMaya.MGlobal.displayError('No export data')
            return
        
        if not self.listwidget.selectedItems():
            OpenMaya.MGlobal.displayWarning('\nNo selection')
            return
            
        for each_item in self.listwidget.selectedItems():            
            if str(each_item.text()) not in self.bundles:
                OpenMaya.MGlobal.displayWarning('\nCorresponding weight not found %s' % each_item.text())
                continue
            
            current_weights = self.bundles[str(each_item.text())]
            
            if current_weights['tag'] == 'cluster':            
                print type(current_weights['data'])
                self.cluster.set_weights(current_weights['data'])
                
            if current_weights['tag'] == 'skinCluster':            
                print current_weights

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Weights(parent=None)
    window.show()
    sys.exit(app.exec_())
