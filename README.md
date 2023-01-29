# ISAT图像分割标注工具

![examples/demo/标注组合图.png](examples/demo/标注组合图.png)

基于多边形的图像分割标注工具，支持实例分割与语义分割。

## 特点
主要对语义标注过程中存在标注重复部分进行优化。
自己标注过分割样本，或者使用coco分割数据集的朋友，肯定遇到过标注多边形之间存在覆盖的问题。
本项目通过引入多边形图层高低的方式，让上层的多边形覆盖下层多边形，从而保证每一个像素的类别都是单一的，降低数据的干扰。

* 支持对多边形图层进行调整(图层置顶或置底)。
* 标注文件转png单通道图(支持实例与语义)。
* 支持滚轮缩放，左键拖动图片。
* 类别标签导入与导出，方便不同任务之间快速切换。

## 导出png单通道图，用于模型训练
![examples/demo/将标注结果导出为png单通道图.png](examples/demo/将标注结果导出为png单通道图.png)
