# -*- coding: utf-8 -*-
# @Author  : LG

from PyQt5 import QtWidgets, QtGui, QtCore
from enum import Enum
from widgets.polygon import Polygon
from configs import DRAWMode
from PIL import Image
import numpy as np


class AnnotationScene(QtWidgets.QGraphicsScene):
    def __init__(self, mainwindow):
        super(AnnotationScene, self).__init__()
        self.mainwindow = mainwindow
        self.image_item:QtWidgets.QGraphicsPixmapItem = None
        self.image_data = None
        self.current_graph:Polygon = None
        self.mode = DRAWMode.VIEW
        self.top_layer = 1

        self.guide_line_x:QtWidgets.QGraphicsLineItem = None
        self.guide_line_y:QtWidgets.QGraphicsLineItem = None

    def load_image(self, image_path):
        self.clear()
        self.image_data = np.array(Image.open(image_path))
        self.image_item = QtWidgets.QGraphicsPixmapItem()
        self.image_item.setZValue(0)
        self.addItem(self.image_item)
        self.image_item.setPixmap(QtGui.QPixmap(image_path))
        self.setSceneRect(self.image_item.boundingRect())
        self.change_mode_to_view()

    def change_mode_to_create(self):
        if self.image_item is None:
            return
        self.mode = DRAWMode.CREATE
        self.image_item.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))

    def change_mode_to_view(self):
        self.mode = DRAWMode.VIEW
        self.image_item.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))

    def change_mode_to_edit(self):
        self.mode = DRAWMode.EDIT
        self.image_item.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))

    def start_draw(self):
        # 只有view模式时，才能切换create模式
        if self.mode != DRAWMode.VIEW:
            return
        # 否则，切换到绘图模式
        self.change_mode_to_create()
        # 绘图模式
        if self.mode == DRAWMode.CREATE:
            self.current_graph = Polygon(self.mainwindow.cfg)
            self.addItem(self.current_graph)

    def finish_draw(self):
        if self.current_graph is None:
            return

        # 移除鼠标移动点
        self.current_graph.removePoint(len(self.current_graph.points) - 1)

        # 单点，删除
        if len(self.current_graph.points) < 2:
            self.current_graph.delete()
            self.removeItem(self.current_graph)
            self.change_mode_to_view()
            return

        # 两点，默认矩形
        if len(self.current_graph.points) == 2:
            first_point = self.current_graph.points[0]
            last_point = self.current_graph.points[-1]
            self.current_graph.removePoint(len(self.current_graph.points)-1)
            self.current_graph.addPoint(QtCore.QPointF(first_point.x(), last_point.y()))
            self.current_graph.addPoint(last_point)
            self.current_graph.addPoint(QtCore.QPointF(last_point.x(), first_point.y()))

        self.change_mode_to_view()
        # 选择类别
        self.mainwindow.category_choice_widget.load_cfg()
        self.mainwindow.category_choice_widget.show()

    def cache_draw(self):
        if self.current_graph is None:
            return
        self.current_graph.delete() # 清除所有路径
        self.removeItem(self.current_graph)

        self.current_graph = None
        self.change_mode_to_view()

    def delete_selected_graph(self):
        deleted_layer = None
        for item in self.selectedItems():
            if item in self.mainwindow.polygons:
                self.mainwindow.polygons.remove(item)
                item.delete()
                self.removeItem(item)
                deleted_layer = item.zValue()
                del item
        if deleted_layer is not None:
            for p in self.mainwindow.polygons:
                if p.zValue() > deleted_layer:
                    p.setZValue(p.zValue() - 1)
            self.mainwindow.labels_dock_widget.update_listwidget()

    def edit_polygon(self):
        selectd_items = self.selectedItems()
        if len(selectd_items) < 1:
            return
        item = selectd_items[0]
        if not item:
            return
        self.mainwindow.category_edit_widget.polygon = item
        self.mainwindow.category_edit_widget.load_cfg()
        self.mainwindow.category_edit_widget.show()

    def move_polygon_to_top(self):
        selectd_items = self.selectedItems()
        if len(selectd_items) < 1:
            return
        current_polygon = selectd_items[0]
        max_layer = len(self.mainwindow.polygons)

        current_layer = current_polygon.zValue()
        for p in self.mainwindow.polygons:
            if p.zValue() > current_layer:
                p.setZValue(p.zValue() - 1)

        current_polygon.setZValue(max_layer)
        for vertex in current_polygon.vertexs:
            vertex.setZValue(max_layer)
        self.mainwindow.set_saved_state(False)

    def move_polygon_to_bottom(self):
        selectd_items = self.selectedItems()
        if len(selectd_items) < 1:
            return
        current_polygon = selectd_items[0]

        if current_polygon is not None:
            current_layer = current_polygon.zValue()

            for p in self.mainwindow.polygons:
                if p.zValue() < current_layer:
                    p.setZValue(p.zValue() + 1)

            current_polygon.setZValue(1)
            for vertex in current_polygon.vertexs:
                vertex.setZValue(1)
        self.mainwindow.set_saved_state(False)

    def mousePressEvent(self, event: 'QtWidgets.QGraphicsSceneMouseEvent'):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            if self.mode == DRAWMode.CREATE:
                sceneX, sceneY = event.scenePos().x(), event.scenePos().y()
                if sceneX < 0:
                    sceneX = 0
                if sceneX > self.width():
                    sceneX = self.width()
                if sceneY < 0:
                    sceneY = 0
                if sceneY > self.height():
                    sceneY = self.height()

                self.current_graph.removePoint(len(self.current_graph.points)-1)
                self.current_graph.addPoint(QtCore.QPointF(sceneX, sceneY))

                # 随鼠标移动的点
                self.current_graph.addPoint(QtCore.QPointF(sceneX, sceneY))
            super(AnnotationScene, self).mousePressEvent(event)

        if event.button() == QtCore.Qt.MouseButton.RightButton:
            if self.mode == DRAWMode.CREATE:
                self.finish_draw()

    def mouseMoveEvent(self, event: 'QtWidgets.QGraphicsSceneMouseEvent'):
        # 辅助线
        if self.guide_line_x is not None and self.guide_line_y is not None:
            if self.guide_line_x in self.items():
                self.removeItem(self.guide_line_x)

            if self.guide_line_y in self.items():
                self.removeItem(self.guide_line_y)

            self.guide_line_x = None
            self.guide_line_y = None

        # 限制在图片范围内
        pos = event.scenePos()
        if pos.x() < 0: pos.setX(0)
        if pos.x() > self.width(): pos.setX(self.width())
        if pos.y() < 0: pos.setY(0)
        if pos.y() > self.height(): pos.setY(self.height())

        if self.mode == DRAWMode.CREATE:
            # 实时移动多边形
            self.current_graph.movePoint(len(self.current_graph.points)-1, pos)

        # 辅助线
        if self.guide_line_x is None and self.width()>0 and self.height()>0:
            self.guide_line_x = QtWidgets.QGraphicsLineItem(QtCore.QLineF(pos.x(), 0, pos.x(), self.height()))
            self.addItem(self.guide_line_x)
        if self.guide_line_y is None and self.width()>0 and self.height()>0:
            self.guide_line_y = QtWidgets.QGraphicsLineItem(QtCore.QLineF(0, pos.y(), self.width(), pos.y()))
            self.addItem(self.guide_line_y)

        # 状态栏,显示当前坐标
        if self.image_data is not None:
            x, y = round(pos.x()), round(pos.y())
            self.mainwindow.labelCoordinates.setText('({}, {}) [{}]'.format(x, y, self.image_data[y-1][x-1]))
        super(AnnotationScene, self).mouseMoveEvent(event)


class AnnotationView(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        super(AnnotationView, self).__init__(parent)
        self.setMouseTracking(True)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.setDragMode(QtWidgets.QGraphicsView.DragMode.ScrollHandDrag)
        self.factor = 1.2

    def wheelEvent(self, event: QtGui.QWheelEvent):
        angel = event.angleDelta()
        angelX, angelY = angel.x(), angel.y()
        point = event.pos() # 当前鼠标位置
        if angelY > 0:
            self.zoom(self.factor, point)
        else:
            self.zoom(1 / self.factor, point)

    def zoom_in(self):
        self.zoom(self.factor)

    def zoom_out(self):
        self.zoom(1/self.factor)

    def zoomfit(self):
        self.fitInView(0, 0, self.scene().width(), self.scene().height(),  QtCore.Qt.AspectRatioMode.KeepAspectRatio)

    def zoom(self, factor, point=None):
        mouse_old = self.mapToScene(point) if point is not None else None
        # 缩放比例

        pix_widget = self.transform().scale(factor, factor).mapRect(QtCore.QRectF(0, 0, 1, 1)).width()
        if pix_widget > 3 or pix_widget < 0.01:
            return

        self.scale(factor, factor)
        if point is not None:
            mouse_now = self.mapToScene(point)
            center_now = self.mapToScene(self.viewport().width() // 2, self.viewport().height() // 2)
            center_new = mouse_old - mouse_now + center_now
            self.centerOn(center_new)
