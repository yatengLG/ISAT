# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/super/PycharmProjects/annotation/ui/file_dock.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(250, 346)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.widget_num = QtWidgets.QWidget(Form)
        self.widget_num.setObjectName("widget_num")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_num)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_current = QtWidgets.QLabel(self.widget_num)
        self.label_current.setText("")
        self.label_current.setObjectName("label_current")
        self.horizontalLayout.addWidget(self.label_current)
        self.label = QtWidgets.QLabel(self.widget_num)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_all = QtWidgets.QLabel(self.widget_num)
        self.label_all.setText("")
        self.label_all.setObjectName("label_all")
        self.horizontalLayout.addWidget(self.label_all)
        self.verticalLayout.addWidget(self.widget_num)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "/"))
