# ISAT图像分割标注工具

![examples/demo/标注组合图.png](examples/demo/标注组合图.png)

基于多边形的图像分割标注工具，支持实例分割与语义分割。

如有快速标注的需求，推荐集成了Segment anything的ISAT：[ISAT_with_segment_anything](https://github.com/yatengLG/ISAT_with_segment_anything)

## 特点
主要对语义标注过程中存在标注重复部分进行优化。
自己标注过分割样本，或者使用coco分割数据集的朋友，肯定遇到过标注多边形之间存在覆盖的问题。
本项目通过引入多边形图层高低的方式，让上层的多边形覆盖下层多边形，从而保证每一个像素的类别都是单一的，降低数据的干扰。

* 支持对多边形图层进行调整(图层置顶或置底)。
* 标注文件转png单通道图(支持实例与语义)。
* 支持滚轮缩放，左键拖动图片。
* 类别标签导入与导出，方便不同任务之间快速切换。
## 安装
### 1. 源码运行
```shell
git clone https://github.com/yatengLG/ISAT.git
cd ISAT
conda create -n ISAT python==3.8
conda activate ISAT
pip install -r requirements.txt
python main.py
```
### 2. 下载打包好的exe
- 2.1 点击[链接](https://github.com/yatengLG/ISAT/releases/download/v1.0.0/ISAT_windows.zip)下载ISAT_windows.zip
- 2.2 解压
- 2.3 双击ISAT/main.exe运行

## 标注结果

### 标注文件与标签图片
ISAT提供了**json格式标注文件**，可以方便的进行传输与二次修改；同时，软件也提供将标注文件转换为**png单通道标签图片**的功能。

#### 1. json格式标注文件
主要用于传输、备份以及二次修改。但不方便直接参与模型训练等过程。

存储信息包括：图片名、图片尺寸、图片额外说明、标注目标类别、标注目标实例id、标注目标多边形顶点等。

#### 2. png单通道标签图片
主要用于模型的训练、测试等过程。

转换后的单通道标签图片具有与原图一致的分辨率，**参与模型训练时，直接读取像素值作为标签即可（图片为单通道图，像素值为单一的值，不是rgb）。**

> 部分软件查看png单通道图片时，存在对颜色边界处进行调整的情况。具体表现为，如  （0， 5， 0）到(0， 255， 0)过渡时，边缘会出现(0， 125， 0)的情况。https://github.com/yatengLG/ISAT/issues/2#issue-1662058434

**最终的标签是图像的像素值，而非颜色值**
这种情况不会对标签图片造成影响，请放心使用。


### 导出png单通道标签图片
软件内置了，将json标注文件转换为png单通道标签图片的工具。

转换时，区分**语义分割**与**实例分割**：
- 语义分割

  转换后的语义分割png单通道标签图片中，每个像素值为对应的类别id，具体的类别含义与标注时类别设置相一致，同时在转换目录中也会留存一份classesition.txt，便于查看类别与id对应关系。
- 实例分割

  转换后的实例分割png单通道标签图片中，每个像素值为对应的组id。
  
![examples/demo/将标注结果导出为png单通道图.png](examples/demo/将标注结果导出为png单通道图.png)
