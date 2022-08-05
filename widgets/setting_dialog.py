# -*- coding: utf-8 -*-
# @Author  : LG

from PyQt5 import QtWidgets, QtCore, QtGui
from ui.setting_dialog import Ui_Dialog
from configs import *
import os


class SettingDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent, mainwindow):
        super(SettingDialog, self).__init__(parent)
        self.mainwindow = mainwindow
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.WindowModality.WindowModal)

        self.init_connect()

    def get_item_and_widget(self, category, color: str):
        item = QtWidgets.QListWidgetItem()
        item.setSizeHint(QtCore.QSize(200, 40))

        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        category_label = QtWidgets.QLabel()
        category_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        category_label.setText(category)
        category_label.setObjectName('category')
        # 颜色
        color_button = QtWidgets.QPushButton()
        color_button.setStyleSheet('QWidget {background-color: %s}' % color)
        color_button.setFixedWidth(30)
        color_button.clicked.connect(self.edit_category_item_color)
        color_button.setObjectName('color')
        # 删除
        delete_button = QtWidgets.QPushButton()
        delete_button.setText('delete')
        delete_button.setFixedWidth(50)
        delete_button.clicked.connect(self.remove_category_item)

        if category == '__background__':
            color_button.setEnabled(False)
            delete_button.setEnabled(False)

        layout.addWidget(category_label)
        layout.addWidget(color_button)
        layout.addWidget(delete_button)
        widget.setLayout(layout)
        return item, widget

    def edit_category_item_color(self):
        button = self.sender()
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            button.setStyleSheet('QWidget {background-color: %s}' % (color.name()))

    def remove_category_item(self):
        button = self.sender()
        row = self.category_list_widget.indexAt(button.parent().pos()).row()
        self.category_list_widget.takeItem(row)

    def load_cfg(self):
        if os.path.exists(CONFIG_FILE):
            cfg = load_config(CONFIG_FILE)
        else:
            cfg = load_config(DEFAULT_CONFIG_FILE)

        self.vertex_hover_size_input.setText(
            '{}'.format(cfg.get('display', {}).get('vertex', {}).get('hover_size', 20)))
        self.vertex_nohover_size_input.setText(
            '{}'.format(cfg.get('display', {}).get('vertex', {}).get('nohover_size', 10)))

        self.polygon_hover_alpha_input.setText(
            '{}'.format(cfg.get('display', {}).get('polygon', {}).get('hover_alpha', 100)))
        self.polygon_nohover_alpha_input.setText(
            '{}'.format(cfg.get('display', {}).get('polygon', {}).get('nohover_alpha', 50)))

        self.category_list_widget.clear()
        labels = cfg.get('label', [])
        labels_key = [l.get('name') for l in labels]

        if '__background__' not in labels_key:
            print(labels)
            labels.insert(0, {'name': '__background__', 'color': '#000000'})

        if labels is not None:
            for label in labels:
                item, item_widget = self.get_item_and_widget(label.get('name', ''), color=label.get('color', '#00ff00'))
                self.category_list_widget.addItem(item)
                self.category_list_widget.setItemWidget(item, item_widget)

    def change_stack_to_display(self):
        self.stackedWidget.setCurrentIndex(0)

    def change_stack_to_label(self):
        self.stackedWidget.setCurrentIndex(1)

    def add_new_category(self):
        category = self.category_input.text()
        color = self.color_button.palette().button().color().name()
        if category:
            item, item_widget = self.get_item_and_widget(category, color)
            self.category_list_widget.addItem(item)
            self.category_list_widget.setItemWidget(item, item_widget)

    def choice_color(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self.color_button.setStyleSheet('QWidget {background-color: %s}' % color.name())

    def import_cfg(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, filter='Yaml File(*.yaml)')
        if file:
            self.mainwindow.reload_cfg(file)
        self.load_cfg()

    def export_cfg(self):
        file, _ = QtWidgets.QFileDialog.getSaveFileName(self, filter='Yaml File(*.yaml)')
        if file:
            self.mainwindow.save_cfg(file)
        self.load_cfg()

    def apply(self):
        cfg = {}
        cfg['display'] = {}
        cfg['display']['vertex'] = {}
        cfg['display']['vertex']['hover_size'] = int(self.vertex_hover_size_input.text())
        cfg['display']['vertex']['nohover_size'] = int(self.vertex_nohover_size_input.text())
        cfg['display']['polygon'] = {}
        cfg['display']['polygon']['hover_alpha'] = int(self.polygon_hover_alpha_input.text())
        cfg['display']['polygon']['nohover_alpha'] = int(self.polygon_nohover_alpha_input.text())
        cfg['label'] = []
        for index in range(self.category_list_widget.count()):
            item = self.category_list_widget.item(index)
            widget = self.category_list_widget.itemWidget(item)
            category_label = widget.findChild(QtWidgets.QLabel, 'category')
            color_button = widget.findChild(QtWidgets.QPushButton, 'color')
            cfg['label'].append(
                {'name': category_label.text(), 'color': color_button.palette().button().color().name()})

        save_config(cfg, CONFIG_FILE)
        self.mainwindow.reload_cfg()
        self.close()

    def cache(self):
        self.close()

    def init_connect(self):
        self.label_button.clicked.connect(self.change_stack_to_label)
        self.display_button.clicked.connect(self.change_stack_to_display)
        self.add_button.clicked.connect(self.add_new_category)
        self.apply_button.clicked.connect(self.apply)
        self.cache_button.clicked.connect(self.cache)
        self.color_button.clicked.connect(self.choice_color)
        self.pushButton_import.clicked.connect(self.import_cfg)
        self.pushButton_export.clicked.connect(self.export_cfg)