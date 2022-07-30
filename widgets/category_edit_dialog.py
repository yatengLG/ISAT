# -*- coding: utf-8 -*-
# @Author  : LG


from ui.category_choice import Ui_Dialog
from PyQt5 import QtWidgets, QtGui, QtCore
from configs import load_config, CONFIG_FILE, DEFAULT_CONFIG_FILE
import os


class CategoryEditDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent, mainwindow, scene):
        super(CategoryEditDialog, self).__init__(parent)

        self.setupUi(self)
        self.mainwindow = mainwindow
        self.scene = scene
        self.polygon = None

        self.lineEdit_group.setValidator(QtGui.QIntValidator(0,1000))

        self.listWidget.itemClicked.connect(self.get_category)
        self.pushButton_apply.clicked.connect(self.apply)
        self.pushButton_cache.clicked.connect(self.cache)

        self.setWindowModality(QtCore.Qt.WindowModality.WindowModal)

    def load_cfg(self):
        self.listWidget.clear()

        labels = self.mainwindow.cfg.get('label', [])

        for label in labels:
            name = label.get('name', 'UNKNOW')
            color = label.get('color', '#000000')
            item = QtWidgets.QListWidgetItem()
            item.setText(name)
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.listWidget.addItem(item)
            if self.polygon is not None and self.polygon.category == name:
                self.listWidget.setCurrentItem(item)
        if self.polygon is None:
            self.lineEdit_group.clear()
            self.lineEdit_category.clear()
            self.checkBox_iscrowded.setCheckState(False)
            self.lineEdit_note.clear()
            self.label_layer.setText('{}'.format(''))
        else:
            self.lineEdit_category.setText('{}'.format(self.polygon.category))
            self.lineEdit_group.setText('{}'.format(self.polygon.group))
            iscrowd = QtCore.Qt.CheckState.Checked if self.polygon.iscrowd == 1 else QtCore.Qt.CheckState.Unchecked
            self.checkBox_iscrowded.setCheckState(iscrowd)
            self.lineEdit_note.setText('{}'.format(self.polygon.note))
            self.label_layer.setText('{}'.format(self.polygon.zValue()))
        if self.listWidget.count() == 0:
            QtWidgets.QMessageBox.warning(self, 'Warning', 'Please set categorys before tagging.')

    def get_category(self, item):
        self.lineEdit_category.setText(item.text())

    def apply(self):
        category = self.lineEdit_category.text()
        group = self.lineEdit_group.text()
        is_crowd = int(self.checkBox_iscrowded.isChecked())
        note = self.lineEdit_note.text()
        if not category:
            QtWidgets.QMessageBox.warning(self, 'Warning', 'Please select one category before submitting.')
            return

        # 设置polygon 属性
        self.polygon.set_drawed(category, group, is_crowd, note,
                                            QtGui.QColor(self.mainwindow.category_color_dict.get(category, '#000000')))
        self.mainwindow.labels_dock_widget.update_listwidget()

        self.polygon = None
        self.scene.change_mode_to_view()
        self.close()

    def cache(self):
        self.scene.cache_draw()
        self.close()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.cache()

    def reject(self):
        self.cache()
