# -*- coding: utf-8 -*-
# @Author  : LG

from PyQt5 import QtWidgets, QtCore, QtGui
from ui.label_dock import Ui_Form
import functools


class LabelsDockWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self, mainwindow):
        super(LabelsDockWidget, self).__init__()
        self.setupUi(self)
        self.mainwindow = mainwindow
        self.polygon_item_dict = {}

        self.listWidget.itemSelectionChanged.connect(self.set_polygon_selected)

        self.listWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.listWidget.customContextMenuRequested.connect(
            self.right_button_menu)

    def right_button_menu(self, point):
        self.mainwindow.right_button_menu.exec_(self.listWidget.mapToGlobal(point))

    def generate_item_and_itemwidget(self, polygon):
        color = self.mainwindow.category_color_dict.get(polygon.category, '#000000')
        item = QtWidgets.QListWidgetItem()
        item.setSizeHint(QtCore.QSize(200, 25))
        item_widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 1, 0, 1)
        check_box = QtWidgets.QCheckBox()
        check_box.setFixedWidth(15)
        check_box.setChecked(polygon.isVisible())
        check_box.stateChanged.connect(functools.partial(self.set_polygon_show, polygon))
        layout.addWidget(check_box)

        label_color = QtWidgets.QLabel()
        label_color.setFixedWidth(10)
        label_color.setStyleSheet("background-color: {};".format(color))
        layout.addWidget(label_color)

        category = QtWidgets.QLabel(polygon.category)
        layout.addWidget(category)

        group = QtWidgets.QLabel('{}'.format(polygon.group))
        layout.addWidget(group)

        iscrowd = QtWidgets.QLabel('crowd') if polygon.iscrowd == 1 else QtWidgets.QLabel(' ')
        layout.addWidget(iscrowd)

        note = QtWidgets.QLabel('{}'.format(polygon.note))
        layout.addWidget(note)

        item_widget.setLayout(layout)
        return item, item_widget

    def update_listwidget(self):
        self.listWidget.clear()
        self.polygon_item_dict.clear()

        for polygon in self.mainwindow.polygons:
            item, item_widget = self.generate_item_and_itemwidget(polygon)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, item_widget)
            self.polygon_item_dict[polygon] = item

        if self.mainwindow.load_finished:
            self.mainwindow.set_saved_state(False)

    def set_selected(self, polygon):
        item = self.polygon_item_dict[polygon]
        if polygon.isSelected():
            if not item.isSelected():
                item.setSelected(True)
        if not polygon.isSelected():
            if item.isSelected():
                item.setSelected(False)

    def set_polygon_selected(self):
        items = self.listWidget.selectedItems()

        have_selected = True if items else False
        self.mainwindow.actionEdit.setEnabled(have_selected)
        self.mainwindow.actionDelete.setEnabled(have_selected)
        self.mainwindow.actionTo_top.setEnabled(have_selected)
        self.mainwindow.actionTo_bottom.setEnabled(have_selected)

        for index, polygon in enumerate(self.mainwindow.polygons):
            if self.polygon_item_dict[polygon] in items:
                if not polygon.isSelected():
                    polygon.setSelected(True)
            else:
                if polygon.isSelected():
                    polygon.setSelected(False)

    def set_polygon_show(self, polygon):
        for vertex in polygon.vertexs:
            vertex.setVisible(self.sender().checkState())
        polygon.setVisible(self.sender().checkState())
