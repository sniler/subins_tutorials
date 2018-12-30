import os
import sys
import warnings

from pprint import pprint

path = '/venture/subins_tutorials'
if path not in sys.path:
    sys.path.append(path)

from PySide import QtGui
from PySide import QtCore
from maya import OpenMaya
from functools import partial
from smartDeform import resources
from smartDeform.utils import read
from smartDeform.utils import generic
from smartDeform.modules import studioMaya
from smartDeform.modules import cluster
from smartDeform.modules import skincluster
reload(studioMaya)
reload(cluster)
reload(skincluster)



class Geometry(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Geometry, self).__init__(parent=None)
        # self.current_item = None
        self.icon_path = resources.getIconPath() 
        
        self.source_path = resources.getInputPath('source_geometry')
        self.target_path = resources.getInputPath('target_geometry')
        
        read_source_data = read.Data(file=self.source_path)
        self.source_data = read_source_data.getData()
        
        read_target_data = read.Data(file=self.target_path)
        self.target_data = read_target_data.getData()
        
        self.source_geometry = None
        self.target_geometry = None
        self.source_deformer = None
        self.target_deformer = None        
        self.source_deformers = None
        self.target_deformers = None
        self.current_deformer = None     
        
        self.my_maya = studioMaya.Maya()
        self.deformer_index = {}       
        self.setupUi()

    def setupUi(self):
        self.setObjectName('geometry')
        self.resize(300, 400)
        
        self.verticallayout = QtGui.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout_')
        self.verticallayout.setSpacing(5)
        self.verticallayout.setContentsMargins(5, 10, 5, 5)       
        
        self.horizontallayout = QtGui.QHBoxLayout(None)
        self.horizontallayout.setObjectName('horizontalLayout')
        self.horizontallayout.setSpacing(5)
        self.horizontallayout.setContentsMargins(0, 0, 0, 0)
        self.verticallayout.addLayout(self.horizontallayout) 

        self.deformer_index = {}
        titles = ['Source', 'Target']
        index = 0
        
        for each_data in [self.source_data, self.target_data]:            
            self.groupbox = QtGui.QGroupBox(self)
            self.groupbox.setObjectName('groupbox_%s' % titles[index])
            self.groupbox.setTitle(titles[index])
            self.horizontallayout.addWidget(self.groupbox) 
            
            self.verticallayout_geometry = QtGui.QVBoxLayout(self.groupbox)
            self.verticallayout_geometry.setObjectName('verticallayout_%s' % titles[index])
            self.verticallayout_geometry.setSpacing(5)
            self.verticallayout_geometry.setContentsMargins(0, 0, 0, 0)
                 
            self.horizontallayout_inputs = QtGui.QHBoxLayout(None)
            self.horizontallayout_inputs.setObjectName('horizontallayout_inputs_%s' % titles[index])
            self.horizontallayout_inputs.setSpacing(1)
            self.horizontallayout_inputs.setContentsMargins(0, 0, 0, 0)
            self.verticallayout_geometry.addLayout(self.horizontallayout_inputs)                 
                 
            self.lineedit = QtGui.QLineEdit(self.groupbox)
            self.lineedit.setObjectName('lineedit_%s' % titles[index])
            self.lineedit.setReadOnly(True)
            self.lineedit.setToolTip('%s Geometry' % titles[index])            
            self.horizontallayout_inputs.addWidget(self.lineedit)
     
            self.button = QtGui.QPushButton(self.groupbox)
            self.button.setObjectName('button_%s' % titles[index])
            self.button.setMinimumSize(QtCore.QSize(25, 25))
            self.button.setMaximumSize(QtCore.QSize(25, 25))
            self.button.setText('+')
            self.button.setToolTip('Add %s Geometry' % titles[index])          
            self.horizontallayout_inputs.addWidget(self.button)
            self.button.clicked.connect(partial (self.add_object, self.lineedit, titles[index]))      
             
            self.combobox = QtGui.QComboBox(self.groupbox)
            self.combobox.setObjectName('combobox_%s' % titles[index])       
            self.combobox.setToolTip('%s Deformers' % titles[index])     
            self.verticallayout_geometry.addWidget(self.combobox)                 
                 
            none_icon_path = os.path.join(self.icon_path, 'none.png')
            none_icon = QtGui.QIcon()
            none_icon.addPixmap(QtGui.QPixmap(none_icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            
            self.combobox.addItem(none_icon, 'None')           
            sort_data = generic.sortDictionary(each_data['data'])
            
            deformer_inputs = {}
            ing = 1    
            for x, items in sort_data.items():
                for each in items:                
                    current_icon_path = os.path.join(self.icon_path, '%s.png' % each)
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(current_icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)                        
                    self.combobox.addItem(icon, each_data['data'][each]['label'])
                    deformer_inputs.setdefault(ing, each)
                    ing += 1
                    
            self.deformer_index.setdefault(titles[index], deformer_inputs)
                    
            self.treewidget = QtGui.QTreeWidget(self.groupbox)
            self.treewidget.setObjectName('treeWidget_%s' % titles[index])
            self.treewidget.setAlternatingRowColors(True)
            self.treewidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
            self.treewidget.setHeaderHidden(True)
            # self.treewidget.setSortingEnabled(True)
            self.treewidget.setToolTip('%s defomer list' % titles[index])
            
            if titles[index]=='Target':
                self.popMenu(self.treewidget)
            
            self.treewidget.itemClicked.connect(partial (self.setDefomerList, self.treewidget, titles[index]))
            self.treewidget.itemSelectionChanged.connect(partial (self.setDefomerList, self.treewidget, titles[index]))
                 
            self.verticallayout_geometry.addWidget(self.treewidget)
            self.combobox.currentIndexChanged.connect(partial (self.setCurrentDeformer, self.lineedit, self.treewidget, titles[index]))             
            index += 1       
            
        self.button = QtGui.QPushButton(self.groupbox)
        self.button.setObjectName('button_convert')
        self.button.setText('Convert')
        self.button.setToolTip('Convert to target deformer')
        self.verticallayout.addWidget(self.button)
        self.button.clicked.connect(self.convert)
        
    
    def popMenu (self, treewidget) :     
        #custom Context Menu        
        treewidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)        
        treewidget.customContextMenuRequested.connect(partial (self.contextMenu, treewidget))

        self.pop_menu    = QtGui.QMenu (self)
        
        self.action_lock = QtGui.QAction(self)
        self.action_lock.setText('Lock Weights')        
        self.pop_menu.addAction (self.action_lock)
        
        self.action_unlock = QtGui.QAction(self)
        self.action_unlock.setText('Unlock Weights')        
        self.pop_menu.addAction (self.action_unlock)
       
    #Right click menu
    def contextMenu (self, treeWidget, point) :
        '''
        index       = self.ui.treeWidget_objectList.indexAt (point)
        if not index.isValid():
            return        
        item        = self.ui.treeWidget_objectList.indexAt (point)
        #self.popMenu.popup (QtGui.QCursor.pos())
        #self.popMenu.exec_ (self.ui.treeWidget_objectList.mapToGlobal(point))
        self.popMenu.exec_ (QtGui.QCursor.pos())
        '''
        
        index = treeWidget.indexAt (point)
        if not index.isValid():
            return        
        
        if self.current_deformer!='skinCluster':
            return
                
        self.pop_menu.exec_ (QtGui.QCursor.pos())      

    
    def add_object(self, lineedit, tag):                
        lineedit.clear()        
        shapes = self.my_maya.getSelectedObjectShapeNode(OpenMaya.MFn.kMesh)        
        if not shapes:
            OpenMaya.MGlobal.displayWarning('not found mesh in your selection!...')   
            return 
                
        lineedit.setText(shapes[-1].partialPathName())
             
        if tag=='Source':            
            self.source_geometry = shapes[-1].partialPathName()
        if tag=='Target':
            self.target_geometry = shapes[-1].partialPathName()
           
            
    def setDefomerList(self, treewidget, tag, *args):
        select_items = treewidget.selectedItems()
        
        defomers = []        
        for each_item in select_items:            
            defomers.append(str(each_item.text(0)))
    
        if tag=='Source':            
            self.source_deformers = defomers
        if tag=='Target':
            self.target_deformers = defomers

        
    def create_items(self, parent, text, icon_name):        
        current_item = QtGui.QTreeWidgetItem(parent, icon_name)            
        iconPath = ''                        
        icon  = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(iconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)                    
        current_item.setIcon(0, icon)
        current_item.setText(0, text)
        return current_item       
            
    def setCurrentDeformer(self, lineedit, treewidget, tag, current_index):        
        current_mesh = str(lineedit.text())
        treewidget.clear()        
        current_deformer_index = self.deformer_index[tag]
        self.current_deformer = current_deformer_index[current_index]
        
        if current_index==0:
            return
        
        if tag=='Source':            
            self.source_deformer = [current_index, current_deformer_index[current_index]]
        if tag=='Target':
            self.target_deformer = [current_index, current_deformer_index[current_index]]        
                 
        if not current_mesh:
            return  
        if current_index not in current_deformer_index:
            return
        if current_deformer_index[current_index] not in self.my_maya.object_types:
            return
        
         
        current_type = self.my_maya.object_types[current_deformer_index[current_index]]        
        deformers = self.my_maya.getDeformerNodes(current_mesh, current_type)       
        deformer_data = {}
        
        if current_deformer_index[current_index]=='blendShape':
            deformers = self.my_maya.getBlenshapeAttributes(deformers)      
        
        if current_deformer_index[current_index]=='skinCluster':
            deformers = self.my_maya.getSkinclusterJoints(deformers[0])
           
        if current_deformer_index[current_index]=='wire':
            deformer_data = {}
            for index in range (deformers.length()):
                curve_objects = self.my_maya.getDeformerNodes(deformers[index], OpenMaya.MFn.kCurve)
                joint_data = self.my_maya.getDeformerJoints(curve_objects)
                cluster_data = self.my_maya.getClusterHandle(curve_objects)
                
                for k, v in joint_data.items():
                    curve_node = OpenMaya.MFnDependencyNode(k)
                    deformer_data.setdefault(curve_node.name(), [])
                    for index in range (v.length()):
                        deformer_data.setdefault(curve_node.name(), []).append(v[index].fullPathName())
                
                for k, v in cluster_data.items():
                    curve_node = OpenMaya.MFnDependencyNode(k)
                    deformer_data.setdefault(curve_node.name(), [])                    
                    for index in range (v.length()):
                        cluster_node = OpenMaya.MFnDependencyNode(v[index])
                        deformer_data.setdefault(curve_node.name(), []).append(cluster_node.name())

        if current_deformer_index[current_index]=='lattice':
            deformer_data = {}
            joint_data = self.my_maya.getDeformerJoints(deformers)            
            cluster_data = self.my_maya.getClusterHandle(deformers)
            
            for k, v in joint_data.items():
                parent_node = OpenMaya.MFnDependencyNode(k)
                for index in range (v.length()):
                    if parent_node.name() in deformer_data:
                        if v[index].fullPathName() in deformer_data[parent_node.name()]:
                            continue
                    deformer_data.setdefault(parent_node.name(), []).append(v[index].fullPathName())
                    
            for k, v in cluster_data.items():
                parent_node = OpenMaya.MFnDependencyNode(k)
                for index in range (v.length()):
                    child_node = OpenMaya.MFnDependencyNode(v[index])
                    if parent_node.name() in deformer_data:
                        if child_node.name() in deformer_data[parent_node.name()]:
                            continue                    
                    deformer_data.setdefault(parent_node.name(), []).append(child_node.name())
            
        if current_deformer_index[current_index]=='cluster':
            for index in range (deformers.length()):  
                mfn_dag_cluster = OpenMaya.MFnDagNode(deformers[index])
                cluster_mobject = mfn_dag_cluster.parent(0)
                cluster_handle = OpenMaya.MFnDependencyNode(cluster_mobject)
                deformer_data.setdefault(cluster_handle.name(), [])
                    
        if not deformer_data:
            for index in range (deformers.length()):
                if isinstance(deformers[index] , OpenMaya.MPlug):
                    deformer_data.setdefault(deformers[index].name(), [])
                
                if isinstance(deformers[index] , OpenMaya.MDagPath):
                    deformer_data.setdefault(deformers[index].fullPathName(), [])

        if not deformer_data:
            return
        
        keys = deformer_data.keys()
        keys.sort()        
        for each_key in keys:
            parent_item = self.create_items(treewidget, each_key, 'test')
            if not deformer_data[each_key]:
                continue
            values = deformer_data[each_key]
            values.sort()            
            for each_value in values:
                child_item = self.create_items(parent_item, each_value, 'test')
            treewidget.setItemExpanded(parent_item, 1)    
        
        #=======================================================================
        # for k, v in deformer_data.items():
        #     parent_item = self.create_items(treewidget, k, 'test')
        #     if not v:
        #         continue
        #     print v
        #     v.sort()
        #     for index in range (len(v)):
        #         child_item = self.create_items(parent_item, v[index], 'test')
        #         print v[index]
        #     treewidget.setItemExpanded(parent_item, 1)          
        #=======================================================================


           
    def convert(self):
        print 'source_geometry', self.source_geometry        
        print 'target_geometry', self.target_geometry
        print 'source_deformers', self.source_deformers
        print 'target_deformers', self.target_deformers

        reload(cluster)
        reload(skincluster)

        if self.target_deformer[0]==1: #  to cluster
            
            if self.source_deformer[0]==5:
                QtGui.QMessageBox.warning(self, 'Warning', 
                        'sorry can not process %s to %s!...' % (self.source_deformer[1], self.target_deformer[1]),
                        QtGui.QMessageBox.Ok)
      
            my_cluster = cluster.Cluster(source_geometry=self.source_geometry, 
                                         target_geometrys=[self.target_geometry],
                                         source_deformers=self.source_deformers, 
                                         target_deformers=self.target_deformers)
                     
            if self.source_deformer[0]==1: #  to softSelection
                try:
                    my_cluster.softSelection()
                except Exception as result:
                    raise Exception(result)
                
            if self.source_deformer[0]==2: #  to blendShape
                try:
                    my_cluster.blendShape()
                except Exception as result:
                   raise Exception(result) 
                       
            if self.source_deformer[0]==3: #  to wire
                try:
                    my_cluster.wire()
                except Exception as result:
                   raise Exception(result) 
                               
            if self.source_deformer[0]==4: #  to lattice
                try:
                    my_cluster.lattice()
                except Exception as result:
                   raise Exception(result) 
                               
            if self.source_deformer[0]==6: #  to skinCluster
                try:
                    my_cluster.skinCluster()
                except Exception as result:
                   raise Exception(result)                 
                
        print self.target_deformer                       
        if self.target_deformer[0]==2: #  to skincluster
            my_skincluster = skincluster.Skincluster(source_geometry=self.source_geometry, 
                                         target_geometrys=[self.target_geometry],
                                         source_deformers=self.source_deformers, 
                                         target_deformers=self.target_deformers)
            
            if self.source_deformer[0]==1: #  to softSelection
                try:
                    my_skincluster.softSelection()
                except Exception as result:
                    raise Exception(result)            

            if self.source_deformer[0]==2: #  to blendShape
                try:
                    my_skincluster.blendShape()
                except Exception as result:
                   raise Exception(result) 
                       
            if self.source_deformer[0]==3: #  to wire
                try:
                    my_skincluster.wire()
                except Exception as result:
                   raise Exception(result)
               
            if self.source_deformer[0]==4: #  to lattice
                try:
                    my_skincluster.lattice()
                except Exception as result:
                   raise Exception(result) 
                               
            if self.source_deformer[0]==5: #  to cluster
                try:
                    my_skincluster.cluster()
                except Exception as result:
                   raise Exception(result)
               

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Geometry(parent=None)
    window.show()
    sys.exit(app.exec_())
