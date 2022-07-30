# -*- coding: utf-8 -*-
# @Author  : LG

from PyQt5 import QtWidgets, QtCore, QtGui
from ui.MainWindow import Ui_MainWindow
from widgets.setting_dialog import SettingDialog
from widgets.category_choice_dialog import CategoryChoiceDialog
from widgets.category_edit_dialog import CategoryEditDialog
from widgets.labels_dock_widget import LabelsDockWidget
from widgets.files_dock_widget import FilesDockWidget
from widgets.info_dock_widget import InfoDockWidget
from widgets.right_button_menu import RightButtonMenu
from widgets.shortcut_dialog import ShortcutDialog
from widgets.about_dialog import AboutDialog
from widgets.converter import ConvertDialog
from widgets.canvas import AnnotationScene, AnnotationView
from configs import ModeEnum, load_config, save_config, CONFIG_FILE, DEFAULT_CONFIG_FILE
from annotation import Object, Annotation
from widgets.polygon import Polygon
import os
from PIL import Image


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.init_ui()

        self.label_root:str = None

        self.files_list: list = []
        self.current_index = None
        self.xml_root: str = None
        self.current_file_index: int = None

        self.saved = True
        self.load_finished = False
        self.polygons:list = []

        self.png_palette = None # 图像拥有调色盘，说明是单通道的标注png文件

        # 标注目标
        self.current_label:Annotation = None

        self.reload_cfg()

        self.init_connect()
        self.reset_action()

    def init_ui(self):

        self.setting_dialog = SettingDialog(parent=self, mainwindow=self)

        self.labels_dock_widget = LabelsDockWidget(mainwindow=self)
        self.labels_dock.setWidget(self.labels_dock_widget)

        self.files_dock_widget = FilesDockWidget(mainwindow=self)
        self.files_dock.setWidget(self.files_dock_widget)

        self.info_dock_widget = InfoDockWidget(mainwindow=self)
        self.info_dock.setWidget(self.info_dock_widget)

        self.scene = AnnotationScene(mainwindow=self)
        self.category_choice_widget = CategoryChoiceDialog(self, mainwindow=self, scene=self.scene)
        self.category_edit_widget = CategoryEditDialog(self, self, self.scene)

        self.convert_dialog = ConvertDialog(self, mainwindow=self)

        self.view = AnnotationView(parent=self)
        self.view.setScene(self.scene)
        self.setCentralWidget(self.view)

        self.right_button_menu = RightButtonMenu(mainwindow=self)
        self.right_button_menu.addAction(self.actionEdit)
        self.right_button_menu.addAction(self.actionTo_top)
        self.right_button_menu.addAction(self.actionTo_bottom)

        self.shortcut_dialog = ShortcutDialog(self)
        self.about_dialog = AboutDialog(self)

        self.labelCoordinates = QtWidgets.QLabel('')
        self.statusbar.addPermanentWidget(self.labelCoordinates)

        self.trans = QtCore.QTranslator()

    def translate(self, language='zh'):
        if language == 'zh':
            self.trans.load('ui/zh_CN')
        else:
            self.trans.load('ui/en')
        _app = QtWidgets.QApplication.instance()
        _app.installTranslator(self.trans)
        self.retranslateUi(self)
        self.info_dock_widget.retranslateUi(self.info_dock_widget)
        self.labels_dock_widget.retranslateUi(self.labels_dock_widget)
        self.files_dock_widget.retranslateUi(self.files_dock_widget)
        self.category_choice_widget.retranslateUi(self.category_choice_widget)
        self.category_edit_widget.retranslateUi(self.category_edit_widget)
        self.setting_dialog.retranslateUi(self.setting_dialog)
        self.about_dialog.retranslateUi(self.about_dialog)
        self.shortcut_dialog.retranslateUi(self.shortcut_dialog)
        self.convert_dialog.retranslateUi(self.convert_dialog)

    def translate_to_chinese(self):
        self.translate('zh')
        self.actionChinese.setChecked(True)
        self.actionEnglish.setChecked(False)
        self.cfg['language'] = 'zh'

    def translate_to_english(self):
        self.translate('en')
        self.actionChinese.setChecked(False)
        self.actionEnglish.setChecked(True)
        self.cfg['language'] = 'en'

    def reload_cfg(self):
        config_file = CONFIG_FILE if os.path.exists(CONFIG_FILE) else DEFAULT_CONFIG_FILE
        self.cfg = load_config(config_file)
        label_dict_list = self.cfg.get('label', [])
        d = {}
        for label_dict in label_dict_list:
            category = label_dict.get('name', 'unknow')
            color = label_dict.get('color', '#000000')
            d[category] = color
        self.category_color_dict = d

        if self.current_index is not None:
            self.show_image(self.current_index)

        language = self.cfg.get('language', 'zh')
        self.translate(language)

    def set_saved_state(self, is_saved:bool):
        self.saved = is_saved
        if self.files_list is not None and self.current_index is not None:

            if is_saved:
                self.setWindowTitle(self.current_label.label_path)
            else:
                self.setWindowTitle('*{}'.format(self.current_label.label_path))

    def open_file(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self)

        if file:
            self.files_list.clear()
            self.files_dock_widget.listWidget.clear()

            self.files_list = [file]
            self.current_index = 0

            if self.label_root is None:
                dir, name = os.path.split(self.files_list[0])
                self.label_root = dir

            self.files_dock_widget.update_widget()
            self.show_image(self.current_index)

    def open_dir(self):
        dir = QtWidgets.QFileDialog.getExistingDirectory(self)
        if dir:
            self.files_list.clear()
            self.files_dock_widget.listWidget.clear()

            files = []
            suffixs = tuple(['{}'.format(fmt.data().decode('ascii').lower()) for fmt in QtGui.QImageReader.supportedImageFormats()])
            for f in os.listdir(dir):
                if f.lower().endswith(suffixs):
                    f = os.path.join(dir, f)
                    files.append(f)
            files = sorted(files)
            self.files_list = files

            self.files_dock_widget.update_widget()

        self.current_index = 0

        if self.label_root is None:
            self.label_root = dir

        self.show_image(self.current_index)

    def save_dir(self):
        dir = QtWidgets.QFileDialog.getExistingDirectory(self)
        if dir:
            self.label_root = dir
        # 刷新图片
        if self.current_index is not None:
            self.show_image(self.current_index)

    def save(self):
        if self.current_label is None:
            return
        self.current_label.objects.clear()
        for polygon in self.polygons:
            object = polygon.to_object()
            self.current_label.objects.append(object)

        self.current_label.note = self.info_dock_widget.lineEdit_note.text()
        self.current_label.save_annotation()
        self.set_saved_state(True)

    def show_image(self, index:int):
        self.reset_action()
        self.current_label = None
        self.load_finished = False
        self.saved = True
        if not -1 < index < len(self.files_list):
            self.scene.clear()
            self.scene.setSceneRect(QtCore.QRectF())
            return
        try:
            self.polygons.clear()
            self.labels_dock_widget.listWidget.clear()
            file_path = self.files_list[index]
            image_data = Image.open(file_path)
            self.png_palette = image_data.getpalette()
            if self.png_palette is not None:
                self.statusbar.showMessage('This is a label file.')
                self.actionCreate.setEnabled(False)
                self.actionSave.setEnabled(False)
                self.actionBit_map.setEnabled(False)

            else:
                self.actionCreate.setEnabled(True)
                self.actionSave.setEnabled(True)
                self.actionBit_map.setEnabled(True)
            self.scene.load_image(file_path)
            self.view.zoomfit()

            # load label
            if self.png_palette is None:
                _, name = os.path.split(file_path)
                label_path = os.path.join(self.label_root, '.'.join(name.split('.')[:-1]) + '.json')
                self.current_label = Annotation(file_path, label_path)
                # 载入数据
                self.current_label.load_annotation()

                for object in self.current_label.objects:
                    polygon = Polygon(self.cfg)
                    self.scene.addItem(polygon)
                    polygon.load_object(object)
                    self.polygons.append(polygon)

            if self.current_label is not None:
                self.setWindowTitle('{}'.format(self.current_label.label_path))
            else:
                self.setWindowTitle('{}'.format(file_path))

            self.labels_dock_widget.update_listwidget()
            self.info_dock_widget.update_widget()
            self.files_dock_widget.set_select(index)
            self.current_index = index
            self.files_dock_widget.label_current.setText('{}'.format(self.current_index+1))
            self.load_finished = True

        except Exception as e:
            print(e)
        finally:
            if self.current_index > 0:
                self.actionPiror.setEnabled(True)
            if self.current_index < len(self.files_list) - 1:
                self.actionNext.setEnabled(True)

    def prior_image(self):
        if self.scene.mode != ModeEnum.VIEW:
            return
        if self.current_index is None:
            return
        if not self.saved:
            result = QtWidgets.QMessageBox.question(self, 'Warning', 'Proceed without saved?', QtWidgets.QMessageBox.StandardButton.Yes|QtWidgets.QMessageBox.StandardButton.No, QtWidgets.QMessageBox.StandardButton.No)
            if result == QtWidgets.QMessageBox.StandardButton.No:
                return
        self.current_index = self.current_index - 1
        if self.current_index < 0:
            self.current_index = 0
            QtWidgets.QMessageBox.warning(self, 'Warning', 'This is the first picture.')
        else:
            self.show_image(self.current_index)

    def next_image(self):
        if self.scene.mode != ModeEnum.VIEW:
            return
        if self.current_index is None:
            return
        if not self.saved:
            result = QtWidgets.QMessageBox.question(self, 'Warning', 'Proceed without saved?', QtWidgets.QMessageBox.StandardButton.Yes|QtWidgets.QMessageBox.StandardButton.No, QtWidgets.QMessageBox.StandardButton.No)
            if result == QtWidgets.QMessageBox.StandardButton.No:
                return
        self.current_index = self.current_index + 1
        if self.current_index > len(self.files_list)-1:
            self.current_index = len(self.files_list)-1
            QtWidgets.QMessageBox.warning(self, 'Warning', 'This is the last picture.')
        else:
            self.show_image(self.current_index)

    def cache_draw(self):
        self.scene.cache_draw()

    def setting(self):
        self.setting_dialog.load_cfg()
        self.setting_dialog.show()

    def add_new_object(self, category, group, segmentation, area, layer, bbox):
        if self.current_label is None:
            return
        object = Object(category=category, group=group, segmentation=segmentation, area=area, layer=layer, bbox=bbox)
        self.current_label.objects.append(object)

    def delete_object(self, index:int):
        if 0 <= index < len(self.current_label.objects):
            del self.current_label.objects[index]

    def change_to_bit_map(self, checked):
        if self.scene.mode == ModeEnum.CREATE:
            self.scenecache_draw()
        if checked:
            for polygon in self.polygons:
                polygon.setEnabled(False)
                for vertex in polygon.vertexs:
                    vertex.setVisible(False)
                polygon.color.setAlpha(255)
                polygon.setBrush(polygon.color)
            self.labels_dock_widget.listWidget.setEnabled(False)
            self.actionCreate.setEnabled(False)
        else:
            for polygon in self.polygons:
                polygon.setEnabled(True)
                for vertex in polygon.vertexs:
                    # vertex.setEnabled(True)
                    vertex.setVisible(polygon.isVisible())
                polygon.color.setAlpha(polygon.nohover_alpha)
                polygon.setBrush(polygon.color)
            self.labels_dock_widget.listWidget.setEnabled(True)
            self.actionCreate.setEnabled(True)

    def label_converter(self):
        self.convert_dialog.reset_gui()
        self.convert_dialog.show()

    def help(self):
        self.shortcut_dialog.show()

    def about(self):
        self.about_dialog.show()

    def exit(self):
        save_config(self.cfg, CONFIG_FILE)
        self.close()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.exit()

    def init_connect(self):
        self.actionOpen.triggered.connect(self.open_file)
        self.actionOpen_dir.triggered.connect(self.open_dir)
        self.actionSave_dir.triggered.connect(self.save_dir)
        self.actionPiror.triggered.connect(self.prior_image)
        self.actionNext.triggered.connect(self.next_image)
        self.actionSetting.triggered.connect(self.setting)
        self.actionExit.triggered.connect(self.exit)

        self.actionCreate.triggered.connect(self.scene.start_draw)
        self.actionEdit.triggered.connect(self.scene.edit_polygon)
        self.actionDelete.triggered.connect(self.scene.delete_selected_graph)
        self.actionSave.triggered.connect(self.save)
        self.actionTo_top.triggered.connect(self.scene.move_polygon_to_top)
        self.actionTo_bottom.triggered.connect(self.scene.move_polygon_to_bottom)

        self.actionZoom_in.triggered.connect(self.view.zoom_in)
        self.actionZoom_out.triggered.connect(self.view.zoom_out)
        self.actionFit_wiondow.triggered.connect(self.view.zoomfit)
        self.actionBit_map.triggered.connect(self.change_to_bit_map)

        self.actionConverter.triggered.connect(self.label_converter)

        self.actionHelp.triggered.connect(self.help)
        self.actionAbout.triggered.connect(self.about)

        self.actionChinese.triggered.connect(self.translate_to_chinese)
        self.actionEnglish.triggered.connect(self.translate_to_english)

        self.labels_dock_widget.listWidget.doubleClicked.connect(self.scene.edit_polygon)

    def reset_action(self):
        self.actionPiror.setEnabled(False)
        self.actionNext.setEnabled(False)
        self.actionCreate.setEnabled(False)
        self.actionEdit.setEnabled(False)
        self.actionDelete.setEnabled(False)
        self.actionSave.setEnabled(False)
        self.actionTo_top.setEnabled(False)
        self.actionTo_bottom.setEnabled(False)
        self.actionBit_map.setChecked(False)
        self.actionBit_map.setEnabled(False)
