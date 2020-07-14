
## 1. 包含：
### 1.1 OpenCv主库
### 2.2 OpenCv贡献库
- bioinspired：生物视觉模块。
- datasets：数据集读取模块。
- dnn：深度神经网络模块。
- face：人脸识别模块。
- matlab:MATLAB接口模块。
- stereo：双目立体匹配模块。
- text：视觉文本匹配模块。
- tracking：基于视觉的目标跟踪模块。
- ximgpro：图像处理扩展模块。
- xobjdetect：增强2D目标检测模块。
- xphoto：计算摄影扩展模块。

## 2.图像处理基础
表示方法： 二值图像，灰度图像，彩色图像(B->G->R)


函数 | 功能 | 参数
---|---|---
cv2.imread(filename, flags=-1)| 读取图像文件| flags:cv2.IMREAD_UNCHANGED=-1 原图像不变；cv2.IMREAD_GRAYSCLE=0...
cv2.namedWindow(winname)| 创建窗口 | 一般会省略这一步
cv2.imshow(winname, mat) | 显示图像 | winname窗口可以存在，也可以不存在
cv2.waitKey(delay=0)|等待按键输入|delay为等待时间
cv2.destoryWindow(winname)|销毁窗口|
cv2.destoryAllWindows()|销毁所有窗口|
cv2.imwrite(filename, img[, params])| 保存图像|
cv2.merge([b, g, r])|通道合并|
a + b | a+b取余：(a+b) % 255 |规则是由于dtype=np.uint8决定的
cv2.add(a, b) | a+b & <=255|
cv2.addWeighted(src1, alpha, src2, beta, gamma) | 图像加权和 | 相当于 saturate(src1 x alpha + src2 x beta + gamma), saturate为取饱和值
cv2.bitwise_and(src1, src2[, mask])|按位与
cv2.bitwise_or(src1, src2[, mask])|按位或
cv2.bitwise_xor(src1, src2[, mask])|按位异或
cv2.bitwise_not(src1, src2[, mask])|按位取反
mask参数 |掩码，操作只会在掩模值为非空的像素点上执行 
