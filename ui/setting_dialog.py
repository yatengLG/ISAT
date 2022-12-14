# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/super/PycharmProjects/ISAT/ui/setting_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(720, 460)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.display_button = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.display_button.setFont(font)
        self.display_button.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.display_button.setAccessibleName("")
        self.display_button.setAutoDefault(False)
        self.display_button.setDefault(False)
        self.display_button.setFlat(True)
        self.display_button.setObjectName("display_button")
        self.verticalLayout.addWidget(self.display_button)
        self.label_button = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_button.setFont(font)
        self.label_button.setFlat(True)
        self.label_button.setObjectName("label_button")
        self.verticalLayout.addWidget(self.label_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_2 = QtWidgets.QWidget(self.page)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.line = QtWidgets.QFrame(self.widget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.verticalLayout_3.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.vertex_hover_size_input = QtWidgets.QLineEdit(self.widget)
        self.vertex_hover_size_input.setMinimumSize(QtCore.QSize(50, 0))
        self.vertex_hover_size_input.setMaximumSize(QtCore.QSize(100, 16777215))
        self.vertex_hover_size_input.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.vertex_hover_size_input.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.vertex_hover_size_input.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.vertex_hover_size_input.setObjectName("vertex_hover_size_input")
        self.gridLayout.addWidget(self.vertex_hover_size_input, 2, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 5, 1, 1)
        self.polygon_nohover_alpha_input = QtWidgets.QLineEdit(self.widget)
        self.polygon_nohover_alpha_input.setMinimumSize(QtCore.QSize(50, 0))
        self.polygon_nohover_alpha_input.setMaximumSize(QtCore.QSize(100, 16777215))
        self.polygon_nohover_alpha_input.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.polygon_nohover_alpha_input.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.polygon_nohover_alpha_input.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.polygon_nohover_alpha_input.setObjectName("polygon_nohover_alpha_input")
        self.gridLayout.addWidget(self.polygon_nohover_alpha_input, 7, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.vertex_nohover_size_input = QtWidgets.QLineEdit(self.widget)
        self.vertex_nohover_size_input.setMinimumSize(QtCore.QSize(50, 0))
        self.vertex_nohover_size_input.setMaximumSize(QtCore.QSize(100, 16777215))
        self.vertex_nohover_size_input.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.vertex_nohover_size_input.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.vertex_nohover_size_input.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.vertex_nohover_size_input.setObjectName("vertex_nohover_size_input")
        self.gridLayout.addWidget(self.vertex_nohover_size_input, 3, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 2, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(60, 0))
        self.label_4.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.polygon_hover_alpha_input = QtWidgets.QLineEdit(self.widget)
        self.polygon_hover_alpha_input.setMinimumSize(QtCore.QSize(50, 0))
        self.polygon_hover_alpha_input.setMaximumSize(QtCore.QSize(100, 16777215))
        self.polygon_hover_alpha_input.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.polygon_hover_alpha_input.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.polygon_hover_alpha_input.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.polygon_hover_alpha_input.setObjectName("polygon_hover_alpha_input")
        self.gridLayout.addWidget(self.polygon_hover_alpha_input, 6, 4, 1, 1)
        self.verticalLayout_3.addWidget(self.widget)
        self.stackedWidget.addWidget(self.page)
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_5 = QtWidgets.QWidget(self.page_1)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.line_2 = QtWidgets.QFrame(self.widget_5)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_5.addWidget(self.line_2)
        self.verticalLayout_6.addWidget(self.widget_5)
        self.category_list_widget = QtWidgets.QListWidget(self.page_1)
        self.category_list_widget.setObjectName("category_list_widget")
        self.verticalLayout_6.addWidget(self.category_list_widget)
        self.widget_3 = QtWidgets.QWidget(self.page_1)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.widget_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        spacerItem2 = QtWidgets.QSpacerItem(58, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.category_input = QtWidgets.QLineEdit(self.widget_3)
        self.category_input.setObjectName("category_input")
        self.horizontalLayout_3.addWidget(self.category_input)
        self.color_button = QtWidgets.QToolButton(self.widget_3)
        self.color_button.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.color_button.setText("")
        self.color_button.setObjectName("color_button")
        self.horizontalLayout_3.addWidget(self.color_button)
        self.add_button = QtWidgets.QPushButton(self.widget_3)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout_3.addWidget(self.add_button)
        self.verticalLayout_6.addWidget(self.widget_3)
        self.stackedWidget.addWidget(self.page_1)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.widget_4 = QtWidgets.QWidget(Dialog)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_import = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_import.setObjectName("pushButton_import")
        self.horizontalLayout.addWidget(self.pushButton_import)
        self.pushButton_export = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_export.setObjectName("pushButton_export")
        self.horizontalLayout.addWidget(self.pushButton_export)
        spacerItem3 = QtWidgets.QSpacerItem(238, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.cache_button = QtWidgets.QPushButton(self.widget_4)
        self.cache_button.setObjectName("cache_button")
        self.horizontalLayout.addWidget(self.cache_button)
        self.apply_button = QtWidgets.QPushButton(self.widget_4)
        self.apply_button.setObjectName("apply_button")
        self.horizontalLayout.addWidget(self.apply_button)
        self.verticalLayout_7.addWidget(self.widget_4)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Setting"))
        self.display_button.setText(_translate("Dialog", "Display"))
        self.label_button.setText(_translate("Dialog", "Label"))
        self.label_8.setText(_translate("Dialog", "Display"))
        self.label_2.setText(_translate("Dialog", "hover size"))
        self.label_3.setText(_translate("Dialog", "nohover size"))
        self.label_6.setText(_translate("Dialog", "hover alpha"))
        self.label.setText(_translate("Dialog", "Vertex"))
        self.label_7.setText(_translate("Dialog", "nohover alpha"))
        self.label_4.setText(_translate("Dialog", "Polygon"))
        self.label_9.setText(_translate("Dialog", "Label"))
        self.label_11.setText(_translate("Dialog", "Add new category"))
        self.add_button.setText(_translate("Dialog", "Add"))
        self.pushButton_import.setText(_translate("Dialog", "Import"))
        self.pushButton_export.setText(_translate("Dialog", "Export"))
        self.cache_button.setText(_translate("Dialog", "Cache"))
        self.apply_button.setText(_translate("Dialog", "Apply"))
