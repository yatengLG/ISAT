# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/super/PycharmProjects/annotation/ui/category_choice.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(286, 264)
        Dialog.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.widget_3 = QtWidgets.QWidget(Dialog)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_category = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_category.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_category.setReadOnly(True)
        self.lineEdit_category.setObjectName("lineEdit_category")
        self.horizontalLayout_3.addWidget(self.lineEdit_category)
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit_group = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_group.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit_group.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_group.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_group.setText("")
        self.lineEdit_group.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_group.setObjectName("lineEdit_group")
        self.horizontalLayout_3.addWidget(self.lineEdit_group)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_5 = QtWidgets.QWidget(Dialog)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lineEdit_note = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_note.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_note.setObjectName("lineEdit_note")
        self.horizontalLayout_5.addWidget(self.lineEdit_note)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.checkBox_iscrowded = QtWidgets.QCheckBox(self.widget)
        self.checkBox_iscrowded.setObjectName("checkBox_iscrowded")
        self.horizontalLayout.addWidget(self.checkBox_iscrowded)
        self.verticalLayout.addWidget(self.widget)
        self.widget_4 = QtWidgets.QWidget(Dialog)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_layer = QtWidgets.QLabel(self.widget_2)
        self.label_layer.setText("")
        self.label_layer.setObjectName("label_layer")
        self.horizontalLayout_2.addWidget(self.label_layer)
        spacerItem1 = QtWidgets.QSpacerItem(97, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_cache = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_cache.setObjectName("pushButton_cache")
        self.horizontalLayout_2.addWidget(self.pushButton_cache)
        self.pushButton_apply = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.horizontalLayout_2.addWidget(self.pushButton_apply)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("Dialog", "category:"))
        self.label.setText(_translate("Dialog", "group:"))
        self.lineEdit_group.setPlaceholderText(_translate("Dialog", "group id"))
        self.label_3.setText(_translate("Dialog", "note:"))
        self.lineEdit_note.setPlaceholderText(_translate("Dialog", "add extra note here"))
        self.checkBox_iscrowded.setText(_translate("Dialog", "is crowded"))
        self.label_4.setText(_translate("Dialog", "layer:"))
        self.pushButton_cache.setText(_translate("Dialog", "cache"))
        self.pushButton_apply.setText(_translate("Dialog", "apply"))
