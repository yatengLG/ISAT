# -*- coding: utf-8 -*-
# @Author  : LG

from PyQt5 import QtCore, QtWidgets, QtGui
from annotation import Object
import typing

class Vertex(QtWidgets.QGraphicsPathItem):
    def __init__(self, polygon, index, color, cfg=None):
        super(Vertex, self).__init__()
        self.polygon = polygon
        self.index = index
        self.color = color
        self.cfg = cfg if cfg is not None else {}

        vertex_cfg = self.cfg.get('display', {}).get('vertex', {})
        self.hover_size = int(vertex_cfg.get('hover_size', 20))
        self.nohover_size = int(vertex_cfg.get('nohover_size', 10))
        self.line_width = 0

        self.nohover = QtGui.QPainterPath()
        self.nohover.addEllipse(QtCore.QRectF(-self.nohover_size//2, -self.nohover_size//2, self.nohover_size, self.nohover_size))
        self.hover = QtGui.QPainterPath()
        self.hover.addEllipse(QtCore.QRectF(-self.hover_size//2, -self.hover_size//2, self.hover_size, self.hover_size))

        self.setPath(self.nohover)
        self.setBrush(self.color)
        self.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.setPen(QtGui.QPen(self.color, self.line_width))
        self.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
        self.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges, True)
        self.setAcceptHoverEvents(True)
        self.setZValue(1e5)

    def itemChange(self, change: 'QtWidgets.QGraphicsItem.GraphicsItemChange', value: typing.Any):

        if change == QtWidgets.QGraphicsItem.GraphicsItemChange.ItemPositionChange and self.isEnabled():
            # 限制顶点移动到图外
            if value.x() < 0:
                value.setX(0)
            if value.x() > self.scene().width():
                value.setX(self.scene().width())
            if value.y() < 0:
                value.setY(0)
            if value.y() > self.scene().height():
                value.setY(self.scene().height())

            self.polygon.movePoint(self.index, value)

        return super(Vertex, self).itemChange(change, value)
    
    def hoverEnterEvent(self, event: 'QGraphicsSceneHoverEvent'):
        self.setPath(self.hover)
        super(Vertex, self).hoverEnterEvent(event)

    def hoverLeaveEvent(self, event: 'QGraphicsSceneHoverEvent'):
        self.setPath(self.nohover)
        super(Vertex, self).hoverLeaveEvent(event)


class Polygon(QtWidgets.QGraphicsPolygonItem):
    def __init__(self, cfg=None):
        super(Polygon, self).__init__(parent=None)

        self.cfg = cfg if cfg is not None else {}
        polygon_cfg = self.cfg.get('display', {}).get('polygon', {})
        self.line_width = 0
        self.hover_alpha = int(polygon_cfg.get('hover_alpha', 100))
        self.nohover_alpha = int(polygon_cfg.get('nohover_alpha', 50))
        self.points = []
        self.vertexs = []
        self.category = ''
        self.group = 0
        self.iscrowd = 0
        self.note = ''

        self.rxmin, self.rxmax, self.rymin, self.rymax = 0, 0, 0, 0 # 用于绘画完成后，记录多边形的各边界，此处与points对应
        self.color = QtGui.QColor('#ff0000')
        self.is_drawing = True

        self.setPen(QtGui.QPen(self.color, self.line_width))
        self.setBrush(QtGui.QBrush(self.color, QtCore.Qt.BrushStyle.FDiagPattern))

        self.setAcceptHoverEvents(True)
        self.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
        self.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges, True)
        self.setZValue(1e5)

    def addPoint(self, point):
        self.points.append(point)
        vertex = Vertex(self, len(self.points)-1, self.color, self.cfg)
        # 添加路径点
        self.scene().addItem(vertex)
        self.vertexs.append(vertex)
        vertex.setPos(point)

    def movePoint(self, index, point):
        if not 0 <= index < len(self.points):
            return
        self.points[index] = self.mapFromScene(point)
        self.redraw()
        if self.scene().mainwindow.load_finished and not self.is_drawing:
            self.scene().mainwindow.set_saved_state(False)

    def removePoint(self, index):
        if not self.points:
            return
        self.points.pop(index)
        vertex = self.vertexs.pop(index)
        self.scene().removeItem(vertex)
        del vertex
        self.redraw()

    def delete(self):
        self.points.clear()
        while self.vertexs:
            vertex = self.vertexs.pop()
            self.scene().removeItem(vertex)
            del vertex

    def moveVertex(self, index, point):
        if not 0 <= index < len(self.vertexs):
            return
        vertex = self.vertexs[index]
        vertex.setEnabled(False)
        vertex.setPos(point)
        vertex.setEnabled(True)

    def itemChange(self, change: 'QGraphicsItem.GraphicsItemChange', value: typing.Any):
        if change == QtWidgets.QGraphicsItem.GraphicsItemChange.ItemSelectedHasChanged and not self.is_drawing: # 选中改变
            self.scene().mainwindow.labels_dock_widget.set_selected(self) # 更新label面板

        if change == QtWidgets.QGraphicsItem.GraphicsItemChange.ItemPositionChange: # ItemPositionHasChanged
            bias = value
            l, t, b, r = self.boundingRect().left(), self.boundingRect().top(), self.boundingRect().bottom(), self.boundingRect().right()
            if l + bias.x() < 0: bias.setX(-l)
            if r + bias.x() > self.scene().width(): bias.setX(self.scene().width()-r)
            if t + bias.y() < 0: bias.setY(-t)
            if b + bias.y() > self.scene().height(): bias.setY(self.scene().height()-b)

            for index, point in enumerate(self.points):
                self.moveVertex(index, point+bias)

            if self.scene().mainwindow.load_finished and not self.is_drawing:
                self.scene().mainwindow.set_saved_state(False)

        return super(Polygon, self).itemChange(change, value)

    def hoverEnterEvent(self, event: 'QGraphicsSceneHoverEvent'):
        if not self.is_drawing:
            self.color.setAlpha(self.hover_alpha)
            self.setBrush(self.color)
        super(Polygon, self).hoverEnterEvent(event)

    def hoverLeaveEvent(self, event: 'QGraphicsSceneHoverEvent'):
        if not self.is_drawing:
            self.color.setAlpha(self.nohover_alpha)
            self.setBrush(self.color)
        super(Polygon, self).hoverEnterEvent(event)

    def mouseDoubleClickEvent(self, event: 'QGraphicsSceneMouseEvent'):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.scene().mainwindow.category_edit_widget.polygon = self
            self.scene().mainwindow.category_edit_widget.load_cfg()
            self.scene().mainwindow.category_edit_widget.show()

    def redraw(self):
        xs = [p.x() for p in self.points]
        ys = [p.y() for p in self.points]
        self.rxmin, self.rymin, self.rxmax, self.rymax = min(xs), min(ys), max(xs), max(ys)
        self.setPolygon(QtGui.QPolygonF(self.points))

    def change_color(self, color):
        self.color = color
        self.color.setAlpha(self.nohover_alpha)
        self.setPen(QtGui.QPen(self.color, self.line_width))
        self.setBrush(self.color)
        for vertex in self.vertexs:
            vertex_color = self.color
            vertex_color.setAlpha(255)
            vertex.setPen(QtGui.QPen(vertex_color, self.line_width))
            vertex.setBrush(vertex_color)

    def set_drawed(self, category, group, iscrowd, note, color:QtGui.QColor, layer=None):
        self.is_drawing = False
        self.category = category
        self.group = group
        self.iscrowd = iscrowd
        self.note = note

        self.color = color
        self.color.setAlpha(self.nohover_alpha)
        self.setPen(QtGui.QPen(self.color, self.line_width))
        self.setBrush(self.color)
        if layer is not None:
            self.setZValue(layer)
        for vertex in self.vertexs:
            vertex_color = self.color
            vertex_color.setAlpha(255)
            vertex.setPen(QtGui.QPen(vertex_color, self.line_width))
            vertex.setBrush(vertex_color)
            if layer is not None:
                vertex.setZValue(layer)

    def calculate_area(self):
        area = 0
        num_points = len(self.points)
        for i in range(num_points):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % num_points]
            d = p1.x() * p2.y() - p2.x() * p1.y()
            area += d
        return abs(area) / 2

    def load_object(self, object):
        segmentation = object.segmentation
        for x, y in segmentation:
            point = QtCore.QPointF(x, y)
            self.addPoint(point)
        color = self.scene().mainwindow.category_color_dict.get(object.category, '#000000')
        self.set_drawed(object.category, object.group, object.iscrowd, object.note, QtGui.QColor(color), object.layer)  # ...

    def to_object(self):
        if self.is_drawing:
            return None
        segmentation = []
        for point in self.points:
            point = point + self.pos()
            segmentation.append((round(point.x()), round(point.y())))
        xmin = self.boundingRect().x() + self.pos().x()
        ymin = self.boundingRect().y() + self.pos().y()
        xmax = xmin + self.boundingRect().width()
        ymax = ymin + self.boundingRect().height()

        object = Object(self.category, group=self.group, segmentation=segmentation,
                        area=self.calculate_area(), layer=self.zValue(), bbox=(xmin, ymin, xmax, ymax), iscrowd=self.iscrowd, note=self.note)
        return object
